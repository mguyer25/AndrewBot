#!/usr/bin/python3

import discord
from discord.ext import commands
import youtube_dl
import os

TOKEN = 'OTcxNjIwNzIyMzY5NzczNTg5.YnNKUA.GVRXUfU02IBYbh10qv19fQaG-to'

bot = commands.Bot(command_prefix = '&')
#client = discord.Client()

@bot.event
async def on_ready():
	print('Bot has successfully logged in as {0.user}'
	.format(bot))

@bot.command(pass_context=True)
async def join(ctx):
	channel = ctx.author.voice.channel
	await channel.connect()

# @client.event
# async def on_message(msg):
# 	print("hello")
# 	if msg.author == client.user:
# 		return
# 	if msg.content.startswith('$hello'):
# 		await msg.channel.send('Let\'s play some wars >:)))) nooooow')

@bot.command(pass_context=True)
async def leave(ctx):
	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
	if voice.is_connected():
		await voice.disconnect()
	else:
		await ctx.send("The bot is not connected to a voice channel.")

@bot.command(pass_context=True)
async def play(ctx, url : str):
	filename = "audio_file.m4a"
	file_there = os.path.isfile(filename)
	
	try:
		if file_there:
			os.remove(filename)
	except PermissionError:
		await ctx.send("Wait for current playing audio to end or use the 'stop' command")
		
	voice_channel = discord.utils.get(ctx.guild.voice_channels, name="general")
	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
	if not voice.is_connected():
		await voice_channel.coonect()

	ydl_opts = {
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key':'FFmpegExtractAudio',
			'preferredcodec': 'm4a',
			'preferredquality': '192',
		}],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])

	for file in os.listdir("./"):
		if file.endswith(".m4a"):
			os.rename(file, filename)
	voice.play(discord.FFmpegPCMAudio(filename, executable='ffmpeg'))
	
@bot.command(pass_context=True)
async def pause(ctx):
	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
	if voice.is_playing():
		voice.pause()
	else:
		await ctx.send("No audio is currently playing.")

@bot.command(pass_context=True)
async def resume(ctx):
	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
	if voice.is_paused():
		voice.resume()
	else:
		await ctx.send("The audio is not paused")

@bot.command(pass_context=True)
async def stop(ctx):
	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
	voice.stop()

bot.run(TOKEN)