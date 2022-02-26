import discord, nacl, ffmpeg, os, random
from discord.ext import commands

client = commands.Bot(command_prefix="coco.")

@client.command()
async def play(ctx, url_: str):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='coconut mall theme')
  await voiceChannel.connect()
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  def repeat():
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: repeat())

  voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: repeat())


@client.command()
async def leave(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_connected():
    await voice.disconnect()

client.run('OTQ2OTU5NjM4MTA3MTM2MDUw.YhmS4w.oigdnKGvt4ArSbGzTNGqz5Rq4M0')