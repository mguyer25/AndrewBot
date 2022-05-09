from click import pass_context
from discord.ext import commands
from utils import config
import discord


class BotJoinLeave(commands.Cog):
    BOT = None

    def __init__(self, bot):
        self.bot = bot
        self.BOT = bot
    
    #@BOT.command(pass_context=True)
    @commands.command(pass_context=True)
    async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    
    #@BOT.command(pass_context=True)
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnet()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    
def setup(bot):
    bot.add_cog(BotJoinLeave(bot))