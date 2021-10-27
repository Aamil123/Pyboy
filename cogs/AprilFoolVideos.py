import discord
from discord.ext import commands
import random
#test

class Fool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def fool(self, ctx):
        videos_link = ["Check out this April Fools' video by google.\n\nhttps://youtu.be/U2JBFlW--UU","Check out this April Fools' video by google.\n\nhttps://youtu.be/VFbYadm_mrw","Check out this April Fools' video by google.\n\nhttps://youtu.be/3MA6_21nka8","Check out this April Fools' video by google.\n\nhttps://youtu.be/dFrgNiweQDk","Check out this April Fools' video by google\n\nhttps://youtu.be/LSZPNwZex9s","Check out this April Fools' video by google.\n\nhttps://youtu.be/Bu927_ul_X0","Check out this April Fools' video by google.\n\nhttps://youtu.be/0_5X6N6DHyk","Check out this April Fools' video by google.\n\nhttps://youtu.be/rznYifPHxDg","Check out this April Fools' video by nvidia.\n\nhttps://youtu.be/smM-Wdk2RLQ","Check out this April Fools' video by razer.\n\nhttps://youtu.be/IlCx5gjAmqI"]
        await ctx.send(random.choice(videos_link))




def setup(bot):
    bot.add_cog(Fool(bot))
#test
