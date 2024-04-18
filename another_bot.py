import discord
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta
import random
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
import asyncio
from discord import Color

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = "'Это бот-пакетик'"

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

    scheduler = AsyncIOScheduler()
    moscow_tz = pytz.timezone('Europe/Moscow')
    scheduler.add_job(send_daily_message, 'cron', hour=1, minute=2, second=0, timezone=moscow_tz)
    scheduler.add_job(send_daily_message_gege, 'cron', hour=1, minute=4, second=0, timezone=moscow_tz)
    scheduler.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "блять" in message.content.lower():
        await message.channel.send("БЛЯТЬ ИРИНА!")
    if "сс" in message.content.lower() or "cс" in message.content.lower() or "сc" in message.content.lower():
        await message.channel.send("Если ты о Саде Спасения, БАН!")
    if "cc" in message.content.lower():
        await message.channel.send("Если ты о Саде Спасения, БАН!")
    if "сад" in message.content.lower() and "спасения" in message.content.lower():
        await message.channel.send("БАН!")
    await bot.process_commands(message)

async def send_daily_message_gege():
    channel = bot.get_channel(1027201347885473852)
    if channel:
        await channel.send("<@user>, а ты в арам?")

async def send_daily_message():
    channel = bot.get_channel(1027201347885473852)
    if channel:
        await channel.send("<@user>, го арам")

@bot.command(name='рольни_двадцатку')
async def roll_dwenty(ctx):
    await ctx.send(random.randint(1, 20))

@bot.command(name='рольни')
async def roll_number(ctx, number: int):
    if number < 0 or number > 100:
        await ctx.send("Ало мы так не работаем, этот пылесос никто не купит")
    else:
        await ctx.send(random.randint(1, number))

@bot.command(name='roll')
async def roll_number_en(ctx, number: int):
    if number < 0 or number > 100:
        await ctx.send("Ало мы так не работаем, этот пылесос никто не купит")
    else:
        await ctx.send(random.randint(1, number))

@bot.command(name='позови')
async def ping_someone(ctx, author):
    for i in range(10):
        await ctx.send(author)

games = ['лига', "хд", "кс", "дестини", "активити в дискорде"]

@bot.command(name='чеделатьбудем')
async def how_dudu(ctx):
    await ctx.send(random.choice(games))

voice_channel = None

channel_id = 0

@bot.command(name="добавь_музыкобота")
async def join(ctx):
    if ctx.author.voice:
        voice_channel = bot.get_channel(channel_id)
        await voice_channel.connect()

@bot.command(name="убери_музыкобота")
async def leave(ctx):
    await ctx.voice_client.disconnect()

from pytube import YouTube
import os
import shutil    

def download_vid(link):
    print("downloading...")
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()  
    if audio_stream:
        audio_stream.download(output_path='music') 
        return os.path.join('music', audio_stream.default_filename)  
    else:
        return None

def delete_audio():
    files = os.listdir('music')
    for my_file in files:
        os.remove(f'music/{my_file}')

def find_music_name():
    return os.listdir('music')[0]

@bot.command(name='остановите_музыку')
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing(): 
        ctx.voice_client.pause() 
        await ctx.send("Ну окей, пауза") 
    else:
        await ctx.send('Ошибочка, тебе надо быть в воисе, чтобы это сделать') 

@bot.command(name="даваймузло")
async def play(ctx,*,link):
    delete_audio()

    download_vid(link) 
    voice_channel = ctx.author.voice.channel

    if not ctx.voice_client:
        voice_channel = await voice_channel.connect() 

    try:
        async with ctx.typing():
            player = discord.FFmpegPCMAudio(executable="ffmpeg", source=f"music/{find_music_name()}") 
            volume_transformed_source = discord.PCMVolumeTransformer(player, volume=0.2)
            ctx.voice_client.play(volume_transformed_source, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send(f'Играет: {find_music_name()}') 

        while ctx.voice_client.is_playing():
            await asyncio.sleep(1)
        delete_audio() 
    except Exception as e:
        print(f'Error: {e}')

@bot.command(name='играй_дальше')
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume() 
        await ctx.send("Играем снова!")
    else:
        await ctx.send('Тебе крч нужно быть в воисе, чтобы запустить эту команду')

@bot.event
async def on_voice_state_update(member, before, after):
    if member == bot.user:
        return None
    if before.channel is None and after.channel is not None:
        await asyncio.sleep(0.5)

        sound_path = "satoru.mp3"  
        audio_source = discord.FFmpegPCMAudio(executable="ffmpeg", source=sound_path)
        voice_client = discord.utils.get(bot.voice_clients, channel=after.channel)
        voice_client.play(audio_source)

commands_list = {
    "/рольни_двадцатку": "ролит d20",
    "/рольни число": "ролит d-число (от 1 до 100)",
    "/roll число": "то же, что и выше",
    "/позови ник человека": "активно зовёт человек",
    "/чеделатьбудем": "выбирает скучающим активность",
    "/добавь_музыкобота": "добавляет бота в голосовой чат, в котором находится вызывающий",
    "/убери_музыкобота": "убирает бота из голосового чата",
    "/давай_музло ссылка на ютуб": "включает музыку в голосовом чатике",
}

@bot.command(name="помощь")
async def give_help_comamnds(ctx):
    string = ""
    for command, description in commands_list.items():
        string += f"`{command}`: {description}\n"
    await ctx.send(string)

bot.run("token")
