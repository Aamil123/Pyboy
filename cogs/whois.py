import discord
from discord.ext import commands


class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['userinfo', 'ui'])
    async def help(self, ctx, member : discord.Member):
        h = ctx.author.avatar_url
        pi = member.avatar_url
        roles = [role.mention for role in member.roles]
        whoisembed = discord.Embed(title = f"{member.name}'s Info", description = f"**:paperclip:TAG:paperclip:**\n`{member.discriminator}`\n\n**:frame_photo:AVATAR:frame_photo: :point_right_tone1:**\n\n**:nazar_amulet:USER ID:nazar_amulet:** \n`{member.id}`\n\n**:inbox_tray:  HIGHEST ROLE :inbox_tray:**\n{member.top_role.mention}\n\n**:busts_in_silhouette:OTHER ROLES:busts_in_silhouette:**\n{roles[0:-1]}\n\n**JOINED :rocket: ON**\n`{member.created_at.strftime('%a %d %B %Y , %I:%M %p UTC')}`\n\n**:bulb: JOINED SERVER ON :bulb: **\n`{member.joined_at.strftime('%a %d %B %Y , %I:%M %p UTC')}`\n\n:robot:BOT:robot:\n`{member.bot}`""")
        whoisembed.set_thumbnail(url = pi)
        whoisembed.set_footer(text=f"Requested By: {ctx.author.display_name}.", icon_url=h)
        await ctx.send(embed=whoisembed)



def setup(bot):
    bot.add_cog(Whois(bot))