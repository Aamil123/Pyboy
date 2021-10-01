import discord
from discord.ext import commands


class BotOnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online now')


def setup(bot):
    bot.add_cog(BotOnReady(bot))