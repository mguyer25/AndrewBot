from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        em = discord.Embed(title="Help", description="Andrew Bot is a multi-use\
             with music and soundboard capabilities.\nCommand calls must start\
             with the '&' character.\nGo ahead and play with the little guy.", 
        colour=discord.Color.blue())

        em.add_field(name="join", value="Join the voice channel that the \
            user calling this command is in")
        em.add_field(name="leave", value="Leave the voice channel that the \
            user calling this command is in")
        em.add_field(name="play <YouTube video URL>", value="Play an audio \
            file from the YouTube URL;\n\twill add to back of queue")
        em.add_field(name="loop", value="WIP: Loops through the current or next \
            song until disabled.")
        em.add_field(name="pause", value="Pauses the current audio that is \
            being played")
        em.add_field(name="resume", value="Resumes audio, if there exists \
            paused audio")
        em.add_field(name="stop", value="Completely stops playing the current \
            audio")
        em.add_field(name="skip", value="WIP: Skips current song")
        em.add_field(name="queue", value="WIP: Shows the queue of songs")
        em.add_field(name="clear_queue", value="WIP: Clears the queue of songs")
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Help(bot))