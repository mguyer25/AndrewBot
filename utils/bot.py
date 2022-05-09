from discord.ext import commands
import discord
from utils import config
import os

class Bot(commands.Bot):

    def __init__(self):
        # Gives access to methods and properties of a parent or sibling class
        super().__init__(
            command_prefix=config.command_prefix, 
            activity=config.starting_activity, 
            help_command=None
        )

        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                # Calls cogs.<filename> like how we call...
                #   'from discord.ext import commands'
                # Slice notation used to copy only the name of the file, 
                #   and not the .py suffix
                self.load_extension(f"cogs.{filename[:-3]}")