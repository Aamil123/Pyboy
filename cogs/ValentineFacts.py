import discord
from discord.ext import commands
import random


class ValentineFact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def valentine_fact(self, ctx):
        valentine_fact = [
        ":heart: **Candlelight din... facts!** :heart:\n\nIn 1868, a British chocolate company called Cadbury created so called 'Fancy Boxes', which essentially were a decorated box of chocolates in the shape of a heart. This set a trend, such that these boxes were quickly associated with Valentine's Day.",":heart: **Love Facts, Episode #42** :heart:\n\nIn 1868, a British chocolate company called Cadbury created so called 'Fancy Boxes', which essentially were a decorated box of chocolates in the shape of a heart. This set a trend, such that these boxes were quickly associated with Valentine's Day.",":heart:  **Love Facts, Episode #42** :heart:\n\nIt's only been roughly 300 years, that the Valentine's Day evolved into what we know today.",":heart: ** Candlelight din... facts!** :heart:\n\nThe earliest Valentine poem known is a rondeau, a form of medieval/renaissance French poetry, composed by Charles, Duke of Orléans to his wife:\n\n""""Je suis desja d'amour tanné,
        Ma tres doulce Valentinée""",":heart: **Love Facts, Episode #42** :heart:\n\nTraditionally, young girls in the U.S. and the U.K. believed they could tell what type of man they would marry depending on the type of bird they saw first on Valentine's Day. If they saw a blackbird, they would marry a clergyman, a robin redbreast indicated a sailor, and a goldfinch indicated a rich man. A sparrow meant they would marry a farmer, a bluebird indicated a happy man, and a crossbill meant an argumentative man. If they saw a dove, they would marry a good man, but seeing a woodpecker meant they would not marry at all."
        ]
        embed = discord.Embed(description = random.choice(valentine_fact))
        await ctx.send(embed=embed)
