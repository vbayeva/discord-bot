import discord
import aiohttp
import io
from discord.ext import commands

class Media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='send_image')
    async def send_image(self, ctx, url: str):
        """Sends an image from given link."""
        if not url:
            return await ctx.send('Please provide an URL.')

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(url)) as response:
                    if response.status == 200:
                        data = await response.read()
                        await ctx.send(file= discord.File(fp=io.BytesIO(data), filename='image.png'))
                    else:
                        await ctx.send("Couldn't retrieve an image.")
        except Exception as e:
            await ctx.send("Coudn't retrieve an image.")

async def setup(bot):
    await bot.add_cog(Media(bot=bot))