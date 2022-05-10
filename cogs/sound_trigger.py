from click import pass_context
from discord.ext import commands
import discord
import youtube_dl
import os

'''
Manages and plays audio files for the soundboard functionality.
'''
class SoundTrigger(commands.Cog):
    # On ?add_sound, check text channel that command was sent in for an audio file
    # to download and add the audio file name to a list of audio filenames
    #
    # Have something that on ?sound <n>, the audio file at index n in the list
    # audio filenames is played
    

    # List of filenames for audio files.
    # The index of the audio file corresponds to
    global sounds_dir
    sounds_dir = "./sounds-lib/"
    global audio_files
    audio_files = []

    def __init__(self, bot):
        self.bot = bot
        for file in os.listdir(sounds_dir):
            audio_files.append(file)

    @commands.command(name="sound", pass_context=True)
    async def play_sound(self, ctx, n : int):
        # n - 1 is an out-of-bounds index of the audio file list 
        if (n > len(audio_files)) or (n <= 0):
            await ctx.send(f"Sound {n} does not exist, try a number " +  
            "in range from 1 to {len(audio_files)}")

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice:
            await ctx.author.voice.channel.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        elif voice.is_playing() or voice.is_pauseed():
            voice.stop()
        filename = (f"{sounds_dir}{audio_files[n - 1]}")
        voice.play(discord.FFmpegPCMAudio(filename, executable='ffmpeg'))
        

    @commands.command(name="play", pass_context=True)
    async def play_url(self, ctx, url):
        filename = "dl_audio.mp3"
        file_there = os.path.isfile(filename)
        try:
            if file_there:
                os.remove(filename)
        except PermissionError:
            await ctx.send("Wait for the currently playing audio to end or " +
            "use the 'stop' command.")

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice:
            await ctx.author.voice.channel.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key':'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
	    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, filename)
        voice.play(discord.FFmpegPCMAudio(filename, executable='ffmpeg'))

        
    """
    Adds a new audio file to the soundboard
    """
    @commands.command(name="add_sound", pass_context=True)
    async def add_sound(self, ctx):
        attachments = ctx.message.attachments
        if len(attachments) != 1:
            await ctx.send("Attach one audio file that you want added to the \
                soundboard with this command.")

        content_type = attachments[0].content_type
        if content_type != "audio/mpeg" and content_type != "audio/ogg":
            await ctx.send("The file attached must be an audio file.")  
        
        new_filename = (f"{len(audio_files) + 1}_{attachments[0].filename}")
        audio_files.append(new_filename)
        await attachments[0].save(f"{sounds_dir}{new_filename}", 
            seek_begin=True, use_cached=False)
     
def setup(bot):
    bot.add_cog(SoundTrigger(bot))