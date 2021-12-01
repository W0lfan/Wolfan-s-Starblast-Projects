import discord
from discord import message
from discord.ext import commands, tasks
from discord.member import Member
import asyncio

from token_generator import *

maps_logs_channel = 878263594435878952

class new:
    async def map(ctx,bot):
        await token.create(maps_logs_channel,bot)
        message = []
        for i in range(0,26):
            for i_ in range(0,26):
                message.append("◼️")
            message.append("\n")
        channel = bot.get_channel(maps_logs_channel)
        print(message)
        await channel.send(''.join([str(elem) for elem in message]))