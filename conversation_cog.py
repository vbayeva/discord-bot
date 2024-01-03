from discord.ext import commands

import utils

class Conversation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='emoji')
    async def emoji(self, ctx):
        """Sends a random emocji"""
        await ctx.send(utils.get_random_emoji())
    
    @commands.command(name='echo')
    async def echo(self, ctx, message='nothing'):
        """Repeats the message providing author and chanell information"""
        ctx_message = ctx.message
        await ctx.send(f"{ctx_message.author} has written {message} at {ctx_message.created_at} in the {ctx_message.channel} chanell")

async def setup(bot):
    await bot.add_cog(Conversation(bot=bot))