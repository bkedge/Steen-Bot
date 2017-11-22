import discord
from discord.ext import commands
from config import TOKEN


description = 'Bot that gets gifs on command'

bot = commands.Bot(command_prefix = '~', description = description)

