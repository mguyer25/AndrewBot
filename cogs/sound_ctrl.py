from click import pass_context
from discord.ext import commands
import discord

class SoundCtrl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="pause", pass_context=True)
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("No audio is currently playing.")

    @commands.command(name="resume", pass_context=True)
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The audio is not paused.")

    @commands.command(name="stop", pass_context=True)
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused() or voice.is_playing():
            voice.stop()
        else:
            await ctx.send("No audio file is currently loaded to stop.")

def setup(bot):
    bot.add_cog(SoundCtrl(bot))