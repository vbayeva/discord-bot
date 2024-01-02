import discord
from discord.ext import commands

import responses

class Numeric(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll')
    async def roll(self, ctx, dice: str = "d6"):
        """Rolls a dice in dN format. For example: /roll d20. If no dice size is provided, default roll size is 6."""

        if dice.startswith('d') and dice[1:].isnumeric():
            dice_size = int(dice[1:])

            result = await responses.get_roll(dice_size)
            await ctx.send(f'You rolled: {result} 🎲!')
        else: 
            await ctx.send('Please specify the dice format as d<number>. For example: /roll d20')

    @commands.command(name='add')
    async def add(self, ctx, first_number: str = None, second_number: str = None):
        if not first_number or not second_number or not first_number.isnumeric() or not second_number.isnumeric():
            return await ctx.send('Please specify the numbers to be added. For example: /add 5 6')
        await ctx.send(int(first_number) + int(second_number))


async def setup(bot):
    await bot.add_cog(Numeric(bot=bot))