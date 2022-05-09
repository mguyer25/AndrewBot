# Run the Juke Bot for music playing capabilities
from utils.keep_alive import keep_alive
from utils.bot import Bot
import os


def main():
    bot = Bot(isjukebot=True)
    TOKEN = os.environ.get("JB_TOKEN") # if this doesn't work, just use TOKEN parser in main_copy.py
    #keep_alive()
    bot.run(TOKEN)

if __name__=="__main__":
    main()