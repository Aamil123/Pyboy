import discord
from discord.ext import commands




class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def say(self, ctx, saymsg = None):
        if saymsg == None:
            await ctx.send(f"Please type any message to send{ctx.athour.mention}")
        await ctx.message.delete()

        e = discord.Embed(description = f"{saymsg}")
        e.set_footer(text=f"said by -{ctx.author.display_name}.", icon_url=ctx.author.avatar_url)
        await ctx.send(embed = e)

    @commands.command()
    async def message(self, ctx, saymsg = None):
        if saymsg == None:
            await ctx.send(f"Please type any message to send{ctx.athour.mention}")
        await ctx.message.delete()
        await ctx.send(saymsg)

def setup(bot):
    bot.add_cog(Say(bot))