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

    @commands.command()
    async def who_is_valentine(self, ctx):
        embed = discord.Embed(description = f"""**Who is Saint Valentine?**\n\nSaint Valentine, officially Saint Valentine of Rome, was a widely recognized 3rd-century christian saint, commemorated on February 14. He was a priest and bishop, ministering persecuted Christians in the Roman Empire, and is associated with a tradition of courtly love since the High Middle Ages, a period commenced around the year 1000AD and lasting until around 1250AD. He was martyred and buried at a Christian cemetery on the Via Flaminia on February 14. \n\nThere are a bunch of inconsistencies in the identification of the saint, however there are evidences for 3 saints that appear in connection with February 14. One of them, Saint Valentine of Terni, is believed to be the one associated with a vision restoration miracle, which happening during his imprisonment. In that, he restored the eyesight of his jailer's daughter, and, on the evening before his execution, supposedly sent her a letter signed with 'Your Valentine' (tuum valentinum). This makes this saint the one we today associate with Saint Valentine's Day. \n\nThe artist Cicero Moraes attempted a facial reconstruction of Saint Valentine, which can be seen in the thumbnail.""",color = 0xFF0DC1)
        embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Saint_Valentine_-_facial_reconstruction.jpg/600px-Saint_Valentine_-_facial_reconstruction.jpg")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ValentineFact(bot))