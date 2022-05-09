# This is for creating a web server to host the bots
# This should be used when running this code on Replit
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Bot running!"

def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()