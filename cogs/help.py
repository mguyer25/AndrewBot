from discord.ext import commands
import discord
from utils import config

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        em = discord.Embed(title="Help", description=f"Andrew Bot is a multi-use\
             with music and soundboard capabilities.\nCommand calls must start\
             with the '{config.command_prefix}' character.\nGo ahead and play \
             with the little guy.", 
        colour=discord.Color.blue())

        em.add_field(name="join", value="Join the voice channel that the \
            user calling this command is in.")
        em.add_field(name="leave", value="Leave the voice channel that the \
            user calling this command is in.")
        em.add_field(name="play <YouTube video URL>", value="Play an audio \
            file from the YouTube URL.")
        em.add_field(name="pause", value="Pauses the current audio that is \
            being played.")
        em.add_field(name="resume", value="Resumes audio, if there exists \
            paused audio.")
        em.add_field(name="stop", value="Completely stops playing the current \
            audio")
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Help(bot))
