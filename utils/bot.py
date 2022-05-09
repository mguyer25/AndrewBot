from discord.ext import commands
import discord

from utils import config
import os

class Bot(commands.Bot):

    def __init__(self, isjukebot : bool):
        self.isjukebot = isjukebot # Whether this bot is a Juke Bot or Soundboard
        super().__init__(
            command_prefix=config.prefix, 
            activity=config.starting_activity, 
            intents=discord.Intents.all(), 
            help_command=None
        )

        # for filename in os.listdir("./cogs"):
        #     if filename.endswith(".py"):
        #         # Calls cogs.<filename> like how we call...
        #         #   'from discord.ext import commands'
        #         # Slice notation used to copy only the name of the file, 
        #         #   and not the .py suffix
        #         self.load_extension(f"cogs.{filename[:-3]}")
        
        bot_cogs_directory = None # String for the path of the cog directory
        if isjukebot:
            bot_cogs_directory = "./jb_cogs"
        else:
            bot_cogs_directory = "./sb_cogs"

        for filename in os.listdir(bot_cogs_directory):
            if filename.endswith(".py"):
                self.load_extension(f"{bot_cogs_directory[2:]}.{filename[:-3]}")