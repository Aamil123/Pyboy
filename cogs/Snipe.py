import discord
from discord.ext import commands
import random


class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    @commands.Cog.listener()
    async def on_message_delete(self ,message):
        self.sniped_messages = {}
        self.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

    
    @commands.command()
    async def snipe(self, ctx):
        try:
            contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]
            
        except:
            await ctx.channel.send("Couldn't find a message to snipe!")
            return

        embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")





def setup(bot):
    bot.add_cog(Snipe(bot))