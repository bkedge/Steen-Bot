import discord
from discord.ext import commands
from config import TOKEN


description = 'Bot that gets gifs on command'

bot = commands.Bot(command_prefix = '~', description = description)

@bot.event
async def on_ready():
    print('Logged in')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

@bot.command()
async def hello():
    """ Says world """
    await bot.say("world")

bot.run(TOKEN)