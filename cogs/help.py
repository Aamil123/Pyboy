import discord
from discord.ext import commands
import asyncio
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    


    @commands.command()
    async def help(self, ctx):
        page1 = discord.Embed(description="\n\n**Fun**\n`.wanted`\n`.tictactoe [user]`\n*This commant is for playing a game name **Tic Tac Toe** this game will start then you can play with using this commant \n`.place [1 to 9]`*\n\n**Maths**\n`.calc`\n*You can do mathematical expressions*\n\n**Help**\n`.help`\n*Shows help for bot commands*\n\n**Information**\n`.user`\n*Returns info about a user.*\n`.server`\n*Returns an embed full of server information.*\n`.whois [Member]`\n*Returns an embed full of that member*\n`.info`\n*You get all information about bot*", colour=discord.Colour.orange())
        page1.set_author(name="Command Help",icon_url="https://image.flaticon.com/icons/png/512/752/752675.png")
        page1.set_thumbnail(url="https://image.flaticon.com/icons/png/512/3254/3254075.png")
        page1.set_footer(text="Page 1 / 3")

        page2 = discord.Embed(description="**Python**\n`.code`\n*How to format Python code on Discord*\n\n**ValentineFacts**\n`.valentine_fact `\n*Shows a random fact about Valentine's Day.*\n`.who_is_valentine`\n*Displays info about Saint Valentine.*\n\n**AprilFoolVideos**\n`.fool`\n*Get a random April Fools' video from Youtube.*\n\n**Fun**\n`.message`\nyou can send the message to that channel using bot\n`.say`\n*Whatever you say the bot will say it*", colour=discord.Colour.orange())
        page2.set_author(name="Command Help",icon_url="https://image.flaticon.com/icons/png/512/752/752675.png")
        page2.set_thumbnail(url="https://image.flaticon.com/icons/png/512/3254/3254075.png")
        page2.set_footer(text="Page 2 / 3")

        page3 = discord.Embed(description="**AvatarModify**\n`.avatar`\n*Show your profile image*\n`.reverse`\n*Reverses the sent text.*\n`.serverlogo`\n*You get the server logo*\n\n**UTILITY**\n`.snipe`\n*You can see the dealed message in the channel*\n`.botinvite`\n*you can invite the bot*\n\n**More Commands coming soon.**", colour=discord.Colour.orange())
        page3.set_author(name="Command Help",icon_url="https://image.flaticon.com/icons/png/512/752/752675.png")
        page3.set_thumbnail(url="https://image.flaticon.com/icons/png/512/3254/3254075.png")
        page3.set_footer(text="Page 3 / 3")

        self.help_pages = [page1, page2, page3]
        buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
        current = 0
        msg = await ctx.send(embed=self.help_pages[current])
        
        for button in buttons:
            await msg.add_reaction(button)
            
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

            except asyncio.TimeoutError:
                return print("test")

            else:
                previous_page = current
                if reaction.emoji == u"\u23EA":
                    current = 0
                    
                elif reaction.emoji == u"\u2B05":
                    if current > 0:
                        current -= 1
                        
                elif reaction.emoji == u"\u27A1":
                    if current < len(self.help_pages)-1:
                        current += 1

                elif reaction.emoji == u"\u23E9":
                    current = len(self.help_pages)-1

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current != previous_page:
                    await msg.edit(embed=self.help_pages[current])
        


def setup(bot):
    bot.add_cog(Help(bot))