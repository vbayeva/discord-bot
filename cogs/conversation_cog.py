import discord
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
    async def joined(self, ctx, member: discord.Member = None):
        """Prints date when member joined the server. If no member provided, shows author's joining date. Example: /when_joined @member_name"""
        if not member:
            member = ctx.author

        join_date = member.joined_at
        formatted_date = utils.get_formatted_date(join_date)

        await ctx.send(f'{member.name} joined this server on {formatted_date}')

    @joined.error
    async def join_date_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found. Please make sure to mention a user correctly!")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Bad argument. Please use the command like this: /joined @username")
        else:
            await ctx.send("An error occurred. Please contact the owner of the server.")

async def setup(bot):
    await bot.add_cog(Conversation(bot=bot))