from PIL import Image,ImageFont,ImageDraw
import sys
import discord
from io import BytesIO
from discord.ext import commands
import random


class imageManuplation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open("wanted-thumblate.jpg")

        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((170, 124))
        wanted.paste(pfp, (10, 70))

        wanted.save("wanted-thumblate.jpg")
        await ctx.send(file = discord.File("wanted-thumblate.jpg"))



def setup(bot):
    bot.add_cog(imageManuplation(bot))