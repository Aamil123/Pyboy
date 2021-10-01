import discord
from discord.ext import commands
import asyncio
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def help(self, ctx):
        await ctx.send("Now i am makking commants")
        


def setup(bot):
    bot.add_cog(Help(bot))