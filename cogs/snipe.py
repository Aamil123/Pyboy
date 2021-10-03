import discord
from discord.ext import commands


class snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        
   lastmsg={}
  
   @commands.Cog.listener() 
   async def on_message_delete(message:discord.Message):
       lastmsg[message.guild.id]=message


  @commands.command()
  async def snipe(ctx:commands.Context):
      try:
          author = lastmsg[ctx.message.guild.id].author.mention
          content = lastmsg[ctx.message.guild.id].content
          channel = lastmsg[ctx.message.guild.id].channel.mention
          embed = discord.Embed(title = ":gun:Hitman Snipes a message!!:gun:\n\n",description = f"**Author**\n{author}\n\n**Message**\n`{content}`\n\n**Channel**\n{channel}\n\n")
          embed.set_footer(text=f"Made by {ctx.author.display_name}.", icon_url=ctx.author.avatar_url)
          await ctx.send(embed = embed)
      except KeyError:
          await ctx.send(f"No Messages to delete in {ctx.channel.mention}")
        
def setup(bot):
    bot.add_cog(snipe(bot))
