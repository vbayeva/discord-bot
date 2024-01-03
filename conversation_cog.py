from discord.ext import commands

import utils

class Conversation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='emoji')
    async def emoji(self, ctx):
        """Sends a random emocji."""
        await ctx.send(utils.get_random_emoji())
    
    @commands.command(name='echo')
    async def echo(self, ctx, message='nothing'):
        """Repeats the message providing author and chanell information."""
        ctx_message = ctx.message
        await ctx.send(f"{ctx_message.author} has written {message} on {utils.get_formatted_date(ctx_message.created_at)} in the {ctx_message.channel} chanell")

    @commands.command(name='when_joined')
    async def join_date(self, ctx):
        """Prints date when you joined the server."""
        member = ctx.author
        join_date = member.joined_at

        formatted_date = utils.get_formatted_date(join_date)

        await ctx.send(f'{member.name} joined this server on {formatted_date}')

async def setup(bot):
    await bot.add_cog(Conversation(bot=bot))