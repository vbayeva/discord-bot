import discord
from discord.ext import commands
from helpers.carbon_footprint_helper import get_random_guide, get_how_to_count_footprint_text
from helpers.segregation_helper import get_where_to_put_item

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
    await bot.load_extension('media_cog')

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def whereToPut(ctx, thing: str):
    """Podpowiada do jakiego pojemnika wrzucić podany rodzaj śmieci. Przykład: $whereToPut metal"""
    await ctx.send(get_where_to_put_item(thing.lower()))

@bot.command()
async def reduceCarbonFootprint(ctx):
    """Porady jak zmniejszyć swój ślad węglowy."""
    await ctx.send(get_random_guide())

@bot.command()
async def howToCountCarbonFootprint(ctx):
    """Pokazuje jak policzyć swój ślad węglowy."""
    for index in range(4):
        await ctx.send(get_how_to_count_footprint_text(index))

bot.run('')
