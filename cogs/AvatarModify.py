import discord
from discord.ext import commands
import typing as t
#TST
class AvatarModify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx):
        pi= ctx.author.avatar_url 
        embed = discord.Embed(title="Your avatar",description="Here is your avatar. I think it looks all cool and 'retro'.")
        embed.set_image(url = pi)
        embed.set_footer(text=f"Made by {ctx.author.display_name}.", icon_url=pi)
        await ctx.send(embed=embed)

    @commands.command()
    async def reverse(self, ctx: commands.Context, *, text: t.Optional[str])-> None:
        if text:
            await ctx.send(f"> {text[::-1]}")
            return

    


def setup(bot):
    bot.add_cog(AvatarModify(bot))
