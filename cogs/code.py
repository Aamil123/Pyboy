import discord
from discord.ext import commands



class Code(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def code(self, ctx):
        embed = discord.Embed(description = """Here's how to format Python code on Discord:\n\n``````py \nprint('Hello world!')\n``````\n\n**These are backticks, not quotes.** Check [this](https://superuser.com/questions/254076/how-do-i-type-the-tick-and-backtick-characters-on-windows/254077#254077) out if you can't find the backtick key.""")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Code(bot))