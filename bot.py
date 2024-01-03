import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = "'This is a sample bot. It can do lots of stuff.'"

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.load_extension('numeric_commands_cog')
    await bot.load_extension('conversation_cog')

bot.run('token')
