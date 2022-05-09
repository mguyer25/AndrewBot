from discord.ext import commands
import discord


class BotJoinLeave(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot has successfully logged in as {0.user}".format(self.bot))

    @commands.command(name="join", pass_context=True)
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    
    @commands.command(name="leave", pass_context=True)
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        #channel = ctx.author.voice.channe
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    
def setup(bot):
    bot.add_cog(BotJoinLeave(bot))