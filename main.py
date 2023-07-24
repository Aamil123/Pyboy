#iam created a awesome pyboy doscprd bot


import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='>', help_command=None)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unloade(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


token = os.environ['token']
bot.run(token)
