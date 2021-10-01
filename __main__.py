import discord
import os
from discord.ext import commands, tasks
import datetime
import random
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO
import asyncio
from discord_components import *
import sys
import typing as t
import wikipedia
import json
import aiohttp
import youtube_dl


bot = commands.Bot(command_prefix = ".",help_command=None)

sad_words = ["sad","bad","low"]

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")



@bot.event
async def on_ready():
    Time = datetime.datetime.now()
    print("we have logged in as {} time {}".format(bot.user,Time))
    DiscordComponents(bot)
    activity = discord.Game(name="Commant: .help", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.event 
async def on_message(message):
    #ctx = await bot.get_context(message)
    if message.author == bot.user:
        return
    if message.content ==".user":
        await message.add_reaction("✅")
        pi= message.author.avatar_url 
        roles = [role.mention for role in message.author.roles]
        embed = discord.Embed(title=f"**{message.author}**",description=(f"\n\n\n\n**User information**\n\nProfile:{message.author.mention}\nID :{message.author.id}\nroles :{roles[1:]}\n"),color=0x016E9A)
        embed.set_thumbnail(url=pi)
        await message.channel.send(embed=embed)
    if message.content == ".nice":
      embed = discord.Embed(description=f"hi{message.author.mention}",color=0x70FF00)
      await message.reply(embed=embed)

    if message.content == ".server":
      await message.add_reaction("✅")
      name = message.guild.name
      icon = message.guild.icon_url
      
      embed = discord.Embed(title="Server Information",description=(f"\n\nServer name : {name}\nID :{message.guild.id}\nRegion : {message.guild.region}\nRoles :{len(message.guild.roles)}\n**Members :{message.guild.member_count}** \n\n**Channels: {len(message.guild.text_channels)+len(message.guild.voice_channels)}**\nVoice :{len(message.guild.voice_channels)}\nText : {len(message.guild.text_channels)}"))
      embed.set_thumbnail(url=icon)
      await message.channel.send(embed=embed)
    if message.content ==  "/About .help":
      embed = discord.Embed(title= ".help",description= f"Hi {message.author.mention} this commant for helpping members")
      await message.channel.send(embed= embed)
    if message.content == ".code":
      await message.add_reaction("✅")
      embed = discord.Embed(description = """Here's how to format Python code on Discord:\n\n``````py \nprint('Hello world!')\n``````\n\n**These are backticks, not quotes.** Check [this](https://superuser.com/questions/254076/how-do-i-type-the-tick-and-backtick-characters-on-windows/254077#254077) out if you can't find the backtick key.""")
      await message.channel.send(embed=embed)
    if message.content == ".valentine_fact":
      await message.add_reaction("✅")
      valentine_fact = [
        ":heart: **Candlelight din... facts!** :heart:\n\nIn 1868, a British chocolate company called Cadbury created so called 'Fancy Boxes', which essentially were a decorated box of chocolates in the shape of a heart. This set a trend, such that these boxes were quickly associated with Valentine's Day.",":heart: **Love Facts, Episode #42** :heart:\n\nIn 1868, a British chocolate company called Cadbury created so called 'Fancy Boxes', which essentially were a decorated box of chocolates in the shape of a heart. This set a trend, such that these boxes were quickly associated with Valentine's Day.",":heart:  **Love Facts, Episode #42** :heart:\n\nIt's only been roughly 300 years, that the Valentine's Day evolved into what we know today.",":heart: ** Candlelight din... facts!** :heart:\n\nThe earliest Valentine poem known is a rondeau, a form of medieval/renaissance French poetry, composed by Charles, Duke of Orléans to his wife:\n\n""""Je suis desja d'amour tanné,
        Ma tres doulce Valentinée""",":heart: **Love Facts, Episode #42** :heart:\n\nTraditionally, young girls in the U.S. and the U.K. believed they could tell what type of man they would marry depending on the type of bird they saw first on Valentine's Day. If they saw a blackbird, they would marry a clergyman, a robin redbreast indicated a sailor, and a goldfinch indicated a rich man. A sparrow meant they would marry a farmer, a bluebird indicated a happy man, and a crossbill meant an argumentative man. If they saw a dove, they would marry a good man, but seeing a woodpecker meant they would not marry at all."
      ]
      embed = discord.Embed(description = random.choice(valentine_fact))
      await message.channel.send(embed=embed)
    if message.content == ".who_is_valentine":
      await message.add_reaction("✅")
      embed = discord.Embed(description = f"""**Who is Saint Valentine?**\n\nSaint Valentine, officially Saint Valentine of Rome, was a widely recognized 3rd-century christian saint, commemorated on February 14. He was a priest and bishop, ministering persecuted Christians in the Roman Empire, and is associated with a tradition of courtly love since the High Middle Ages, a period commenced around the year 1000AD and lasting until around 1250AD. He was martyred and buried at a Christian cemetery on the Via Flaminia on February 14. \n\nThere are a bunch of inconsistencies in the identification of the saint, however there are evidences for 3 saints that appear in connection with February 14. One of them, Saint Valentine of Terni, is believed to be the one associated with a vision restoration miracle, which happening during his imprisonment. In that, he restored the eyesight of his jailer's daughter, and, on the evening before his execution, supposedly sent her a letter signed with 'Your Valentine' (tuum valentinum). This makes this saint the one we today associate with Saint Valentine's Day. \n\nThe artist Cicero Moraes attempted a facial reconstruction of Saint Valentine, which can be seen in the thumbnail.""",color = 0xFF0DC1)
      embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Saint_Valentine_-_facial_reconstruction.jpg/600px-Saint_Valentine_-_facial_reconstruction.jpg")
      await message.channel.send(embed=embed)
      if "<@869887033454264330>" in message.content:
        await message.channel.send("SILLY PINGER!!!")
      await bot.process_commands(message)
    if message.content == ".fool":
      await message.add_reaction("✅")
      videos_link = ["Check out this April Fools' video by google.\n\nhttps://youtu.be/U2JBFlW--UU","Check out this April Fools' video by google.\n\nhttps://youtu.be/VFbYadm_mrw","Check out this April Fools' video by google.\n\nhttps://youtu.be/3MA6_21nka8","Check out this April Fools' video by google.\n\nhttps://youtu.be/dFrgNiweQDk","Check out this April Fools' video by google\n\nhttps://youtu.be/LSZPNwZex9s","Check out this April Fools' video by google.\n\nhttps://youtu.be/Bu927_ul_X0","Check out this April Fools' video by google.\n\nhttps://youtu.be/0_5X6N6DHyk","Check out this April Fools' video by google.\n\nhttps://youtu.be/rznYifPHxDg","Check out this April Fools' video by nvidia.\n\nhttps://youtu.be/smM-Wdk2RLQ","Check out this April Fools' video by razer.\n\nhttps://youtu.be/IlCx5gjAmqI"]
      await message.channel.send(random.choice(videos_link))
    if message.content == ".avatar":
      await message.add_reaction("✅")
      pi= message.author.avatar_url 
      embed = discord.Embed(title="Your avatar",description="Here is your avatar. I think it looks all cool and 'retro'.")
      embed.set_image(url = pi)
      embed.set_footer(text=f"Made by {message.author.display_name}.", icon_url=pi)
      await message.channel.send(embed=embed)
    if message.content == ('.help'):
        user=message.author
        msg = "please invite pyboy to your server and support us"
        embed = discord.Embed(title = "Helpful links",description = """[Invite link](https://discord.com/api/oauth2/authorize?client_id=869887033454264330&permissions=8&scope=bot)\n\nAnd if your uncomfortable with the admin perms the bot is required, just dm me i can specify the perms :wink:
        our owner user id `Aamil ᓚᘏᗢ#0419`""")
        await user.send(msg)
        await user.send(embed=embed)
    if message.content == bot.user.mention:
      embed = discord.Embed(title="You Silly Pinger!!",description="Type `.help` for more......silly pinger")
      embed.set_footer(text=f"{message.author.display_name}.",icon_url=pi)
    if message.content == "test":
      await message.delete(message.content)
    if message.content == "!DM":
      await message.channel.send("hello")
    await bot.process_commands(message)

lastmsg={}
@bot.event
async def on_message_delete(message:discord.Message):
  lastmsg[message.guild.id]=message


@bot.command()
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

@bot.command()
async def test(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.athour


  wanted = Image.open("wanted-poster-template-3c78a107d0d610d5fa6ca1cbf779f8cc.jpg")

  asset = user.avatar_url_as(size = 128)
  data = BytesIO(await asset.read())
  pfb = Image.open(data)

  pfb = pfb.resize((177,177))

  wanted.paste(pfb,(120,212))

  wanted.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))


# help pages
page1 = discord.Embed(description="\n\n**Fun**\n`.wanted`\n`.tictactoe [user]`\n*This commant is for playing a game name **Tic Tac Toe** this game will start then you can play with using this commant \n`.place [1 to 9]`*\n\n**Maths**\n`.calc`\n*You can do mathematical expressions*\n\n**Help**\n`.help`\n*Shows help for bot commands*\n\n**Information**\n`.user`\n*Returns info about a user.*\n`.server`\n*Returns an embed full of server information.*\n`.whois [Member]`\n*Returns an embed full of that member*", colour=discord.Colour.orange())
page1.set_author(name="Command Help",icon_url="https://image.flaticon.com/icons/png/512/752/752675.png")
page1.set_thumbnail(url="https://image.flaticon.com/icons/png/512/3254/3254075.png")

page2 = discord.Embed(description="**Python**\n`.code`\n*How to format Python code on Discord*\n\n**ValentineFacts**\n`.valentine_fact `\n*Shows a random fact about Valentine's Day.*\n`.who_is_valentine`\n*Displays info about Saint Valentine.*\n\n**AprilFoolVideos**\n`.fool`\n*Get a random April Fools' video from Youtube.*\n\n**Fun**\n`.message`\nyou can send the message to that channel using bot", colour=discord.Colour.orange())
page2.set_author(name="Command Help",icon_url="https://image.flaticon.com/icons/png/512/752/752675.png")
page2.set_thumbnail(url="https://image.flaticon.com/icons/png/512/3254/3254075.png")

page3 = discord.Embed(description="**AvatarModify**\n`.avatar`\n*Show your profile image*\n`.reverse`\n*Reverses the sent text.*\n\n**UTILITY**\n`.snipe`\n*You can see the dealed message in the channel*\n\n**More Commands coming soon.**", colour=discord.Colour.orange())
page3.set_author(name="Command Help",icon_url="https://image.flaticon.com/icons/png/512/752/752675.png")
page3.set_thumbnail(url="https://image.flaticon.com/icons/png/512/3254/3254075.png")

bot.help_pages = [page1, page2, page3]

@bot.group(invoke_without_command=True)
async def help(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

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
                if current < len(bot.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.help_pages[current])

@help.command()
async def snipe(ctx):
   em = discord.Embed(title = "Help for `.snipe`",description = f"The `.snipe` commant is *you can see dealed message on that channel*.\nLike this :point_down:\n\n")
   em.set_image(file=discord.File('attachment://Screenshot from 2021-08-28 19-07-46.png'))
   await ctx.send(embed = em)

@bot.command(help = "To make someone wanted!")
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted-poster-template-3c78a107d0d610d5fa6ca1cbf779f8cc.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((170, 124))
    wanted.paste(pfp, (10, 70))

    wanted.save("wanted-poster-template-3c78a107d0d610d5fa6ca1cbf779f8cc.jpg")
    await ctx.send(file = discord.File("wanted-poster-template-3c78a107d0d610d5fa6ca1cbf779f8cc.jpg"))



player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]
 
#calculates answer
def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred.'
    return result
 
@bot.command()
async def calc(ctx):
    m = await ctx.send(content='Loading Calculators...')
    expression = 'None'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'{ctx.author.name}\'s calculator | {ctx.author.id}', description=expression,
                        timestamp=delta)
    await m.edit(components=buttons, embed=e)
    while m.created_at < delta:
        res = await bot.wait_for('button_click')
        if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
            0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == 'None' or expression == 'An error occurred.':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed', type=7)
                break
            elif res.component.label == '←':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression = 'None'
            elif res.component.label == '=':
                expression = calculate(expression)
            else:
                expression += res.component.label
            f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression,
                                timestamp=delta)
            await res.respond(content='', embed=f, components=buttons, type=7)



@bot.command()
async def reverse(ctx: commands.Context, *, text: t.Optional[str]) -> None:
        """
        Reverses the sent text.
        If no text is provided, the user's profile picture will be reversed.
        """
        if text:
            await ctx.send(f"> {text[::-1]}")
            return

@bot.command(aliases = ['userinfo', 'ui'])
async def whois(ctx, member : discord.Member):
    h = ctx.author.avatar_url
    pi = member.avatar_url
    roles = [role.mention for role in member.roles]
    whoisembed = discord.Embed(title = f"{member.name}'s Info", description = f"**:paperclip:TAG:paperclip:**\n`{member.discriminator}`\n\n**:frame_photo:AVATAR:frame_photo: :point_right_tone1:**\n\n**:nazar_amulet:USER ID:nazar_amulet:** \n`{member.id}`\n\n**:inbox_tray:  HIGHEST ROLE :inbox_tray:**\n{member.top_role.mention}\n\n**:busts_in_silhouette:OTHER ROLES:busts_in_silhouette:**\n{roles}\n\n**JOINED :rocket: ON**\n`{member.created_at.strftime('%a %d %B %Y , %I:%M %p UTC')}`\n\n**:bulb: JOINED SERVER ON :bulb: **\n`{member.joined_at.strftime('%a %d %B %Y , %I:%M %p UTC')}`""")
    whoisembed.set_thumbnail(url = pi)
    whoisembed.set_footer(text=f"Requested By: {ctx.author.display_name}.", icon_url=h)
    await ctx.send(embed=whoisembed)



@bot.command(aliases = ['Message', 'm'])
async def message(ctx, saymsg = None):
    if saymsg == None:
      await ctx.send(f"Please type any message to send{ctx.athour.mention}")
    await ctx.message.delete()
    await ctx.send(saymsg)


@bot.command(pass_context=True)
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=API_KEY_GOES_HERE')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=API_KEY_GOES_HERE&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await bot.send_message(embed=embed)




@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


@bot.command()
async def text(ctx, *, text = "No text entered"):
    img = Image.open("1hzypv.jpg")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 24)

    draw.text((0,150), text, (0, 0, 0), font=font)

    img.save("1hzypv.jpg")

    await ctx.send(file = discord.File("1hzypv.jpg"))



def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
@commands.is_owner()
async def reboot(ctx):
  await ctx.send("Rebooting bot...")
  restart_bot()


bot.run("ODY5ODg3MDMzNDU0MjY0MzMw.YQEvbg.4mwn-IzkW5PtqqhroU7DOvWKszo")