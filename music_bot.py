import os
import discord
from discord.ext import commands
import youtube_dl
from discord import Intents

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx, url):
    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

        voice_client = ctx.voice_client

        # Проверьте, подключен ли бот к голосовому каналу
        if voice_client is None:
            # Если нет, подключитесь к голосовому каналу автора сообщения
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()

        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice_client.stop()
        voice_client.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = 0.1


@bot.command()
async def pause(ctx):
    ctx.voice_client.pause()

@bot.command()
async def resume(ctx):
    ctx.voice_client.resume()

@bot.command()
async def stop(ctx):
    ctx.voice_client.stop()

bot.run(os.environ['BOT_TOKEN'])
