import discord
import responses
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = "'This is a sample bot. It can do lots of stuff.'"

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command(name='roll')
async def hello(ctx, dice: str = ""):
    """Rolls a dice in dN format. For example: /roll d20. If no dice size is provided, default roll size is 6."""
    if not dice:
        result = await responses.get_roll()
        await ctx.send(f'You rooled is: {result} 🎲!')
        return

    if dice.startswith('d') and dice[1:].isnumeric():
        dice_size = int(dice[1:])

        result = await responses.get_roll(dice_size)
        await ctx.send(f'You rolled: {result} 🎲!')
    else: 
        await ctx.send('Please specify the dice format as d<number>. For example: /roll d20')
    

bot.run('token')
