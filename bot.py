import discord
from discord.ext import commands
import giphypop
from giphypop import translate
from config import TOKEN



description = 'Bot that gets gifs on command'

bot = commands.Bot(command_prefix = '$', description = description)

g = giphypop.Giphy()



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

@bot.command()
async def gif(*, message: str):
    """ Fetches gif """
    img = translate(message)
    url = img.url
    await bot.say(url)
    
bot.run(TOKEN)