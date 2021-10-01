import discord
from discord.ext import commands


class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx):
        name = ctx.guild.name
        icon = ctx.guild.icon_url
        embed = discord.Embed(title="Server Information",description=f"\n\n:name_badge: **SERVER NAME** :name_badge:\n`{name}`\n\n:id: **ID** :id:\n`{ctx.guild.id}`\n\n:placard: **REGION** :placard:\n`{ctx.guild.region}`\n\n:busts_in_silhouette:**ROLES**:busts_in_silhouette:\n`{len(ctx.guild.roles)}`\n\n:busts_in_silhouette: **Members** :busts_in_silhouette:\n `{ctx.guild.member_count}`\n\n:inbox_tray: **Channels** :inbox_tray:\n`{len(ctx.guild.text_channels)+len(ctx.guild.voice_channels)}`\n\n:loud_sound:**Voice**:loud_sound:\n`{len(ctx.guild.voice_channels)}`\n\n:blue_book: **Text** :blue_book:\n`{len(ctx.guild.text_channels)}`")
        embed.set_thumbnail(url=icon)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Whois(bot))