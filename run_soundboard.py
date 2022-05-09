# Runs the sounboard bot for Andrew >:)
#from utils.keep_alive import keep_alive
from utils.bot import Bot
from discord.ext import commands

def main():
    bot = Bot()
    key = None
    token = None # This is the authentication token of the bot
    with open('./.env') as f:
        for line in f:
            key, token = line.strip().split('=', 1)
            break
    
    if (token):
        bot.run(token)
    else:
        print("There exists no .env with a authentication token for the bot \
        in the directory that contains run_soundboard.py.\n")


if __name__=="__main__":
    main()