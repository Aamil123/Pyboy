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

#just test

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


with open("token.0", "r", encoding="utf-8") as f:
    Token = f.read()


bot.run(Token)
