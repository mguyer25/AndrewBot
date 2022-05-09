# Runs the sounboard bot for Andrew >:)
from utils.keep_alive import keep_alive
from utils.bot import Bot
import os

def main():
    bot = Bot(isjukebot=False)
    TOKEN = os.environ.get("SB_TOKEN") # if this doesn't work, just use TOKEN parser in main_copy.py
    #keep_alive()
    bot.run(TOKEN)


if __name__=="__main__":
    main()