import discord
from discord import message
from discord.ext import commands, tasks
from discord_buttons_plugin import *
import random
from random import randrange
import asyncio
from discord.ext.commands.core import command
from asyncio import TimeoutError
import re
from discord_components.ext.filters import channel_filter
intents = discord.Intents.default()
intents.members = True
from discord import ChannelType
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions

from mine import Mine
from token_generator import token
from newMap import *

bot = commands.Bot(command_prefix='?', case_insensitive = True)
bot.remove_command('help')
bot.remove_command('rules')
buttons = ButtonsClient(bot)

#   python C:\Users\Utilisateur\Desktop\Miner_bot\main.py
@bot.event
async def on_ready():
    print('Bot started.')


@bot.command()
async def mine(ctx, amount:int):
    Mine.Mine(ctx,amount)

@bot.command()
async def test(ctx):
    await new.map(ctx,bot)

bot.run('')
