from asyncio.windows_events import NULL
from os import stat
import discord
from discord import message
from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.errors import MissingRequiredArgument
from discord.member import Member
import random
from random import randrange
import asyncio
from discord.ext.commands.core import command
from asyncio import TimeoutError
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
import math
import requests
import re

bot = commands.Bot(command_prefix='?', case_insensitive = True)
bot.remove_command('help')
bot.remove_command('rules')

# python C:\Users\Utilisateur\Desktop\Bot\main.py
@bot.event
async def on_ready():
    print("Bot ready.")
    channel = bot.get_channel(882525850594070549)
    await channel.send('I am now online.')
    database_handler.reset()
from Database.handler import DatabaseHandler
database_handler = DatabaseHandler("database.db")


@bot.event
async def on_ready():
    print('Ready.')

@bot.event
async def on_message(message):
    if message.author.id != 887711314590437436:
        asJoined = database_handler.returnValue('user_id',message.author.id)
        if asJoined == False:
            database_handler.createStatus(message.author.id, f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
        else:
            messages = database_handler.returnValue("xp",str(message.author.id))
            database_handler.modify(message.author.id,"xp",messages + 1)
            messages = database_handler.returnValue("xp",str(message.author.id))
            level = database_handler.returnValue("level",str(message.author.id))
            if messages / 1000 == level + 1:
                colors = [
                        0xF14141,
                        0xEAF328,
                        0x31F328,
                        0x28F3C8,
                        0x2881F3,
                        0xC528F3,
                        0xF3287B
                ]
                quotes = [
                        "💪 Nothing can stop you!",
                        "💨 Typing as fast as light speed!",
                        "👀 Damn what an activity!",
                        f"👁️ Big {message.author.name} is watching you!",
                        "🤯 So many messages!"
                ]
                embed = discord.Embed(
                    color = random.choice(colors),
                    title = f"{message.author.name} 🎉 | Congratulations, you won a level!",
                    description = f"You are now level **{level + 1}**!\n\n**{random.choice(quotes)}**"
                )
                embed.set_author(
                    name = message.author.name,icon_url=message.author.avatar_url
                )
                levels = [
                        [30.0,50.0,70.0],
                        [
                            "the reaction role! It allows you to react to any message!",
                            "a custom color role (unchangable, choose wisely)!",
                            "to get a free ECP key (if you don't already have one)!"
                        ],
                ]
                for level_ in levels[0]:
                    if messages / 1000 == level_:
                        embed.add_field(
                                name = "🎁 What's that? You won a gift!",
                                value = f"To thanks you for your activity, here is a gift: you won {levels[1][levels[0].index(messages/1000)]}"
                        )
                        if level_ == 30:
                            role = discord.utils.get(message.guild.roles,name="@reaction")
                            await message.author.add_roles(role)
                database_handler.modify(message.author.id,"level",level + 1)
                await message.channel.send(embed = embed)
    await bot.process_commands(message)

@bot.command()
async def role(ctx, code, *name):
    fullName = " ".join(name)
    level = database_handler.returnValue("level",str(ctx.author.id))
    has_custom_role = database_handler.returnValue("has_custom_role",str(ctx.author.id))
    length = len(fullName.split())
    if length <= 15:
        if level >= 50: 
            if has_custom_role != True:
                if "0x" in code:
                    code = int(code,16)
                    embed = discord.Embed(
                        title = f"🧐 Interesting role, {ctx.message.author.name}",
                        description = f"Are you sure you want to create a custom role named '{fullName}' with color {code}?"
                    )
                    embed.set_author(
                        name = ctx.author.name,icon_url=ctx.author.avatar_url
                    )                
                    message = await ctx.send(embed = embed)
                    def checkEmoji(reaction,user):
                        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "❌" or str(reaction.emoji) == "✔️")
                    await message.add_reaction("❌")
                    await message.add_reaction("✔️")
                    reaction, user = await bot.wait_for(
                        "reaction_add", timeout = 120, check = checkEmoji
                    )
                    if reaction.emoji == "❌":
                        await ctx.send("Canceled the action!")
                    if reaction.emoji == "✔️":
                        role = await ctx.guild.create_role(name=f'[{fullName}]',colour=discord.Colour(code))
                        await ctx.message.author.add_roles(role)
                        embed = discord.Embed(
                            title = f"Successfully created {ctx.author.name}'s custom color!",
                            description = f"What a neat color ✨\nYour wonderful <@&{role.id}> role has been created! Enjoy!"
                        )
                        await ctx.send(embed = embed)
                        database_handler.modify(ctx.author.id,"has_custom_role",True)
                else:
                    embed = discord.Embed(
                        title = "Error: wrong color code",
                        description = "Correct code can be taken [here](https://www.w3schools.com/colors/colors_picker.asp).\nUsage: `0xHTMLCODE`"
                    )
                    embed.set_author(
                        name = ctx.author.name,icon_url=ctx.author.avatar_url
                    )         
                    await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    title = "Error: you already have a custom role!",
                    description = "** **"
                )
                embed.set_author(
                    name = ctx.author.name,icon_url=ctx.author.avatar_url
                )         
                await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = "Error: your level is not high enough!",
                description = f"Your level must be equal or higher than **50**. Your level is currently **{level}**."
            )
            embed.set_author(
                name = ctx.author.name,icon_url=ctx.author.avatar_url
            )         
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(
            title = "Error: your role name has too much characters!",
            description = f"Your role name must be less or equal than 20 characters."
        )
        embed.set_author(
            name = ctx.author.name,icon_url=ctx.author.avatar_url
        )         
        await ctx.send(embed = embed)
@bot.command()
async def rank(ctx,user:discord.Member = None):
    if not user:
        user = ctx.author
    colors = [
        0xF14141,
        0xEAF328,
        0x31F328,
        0x28F3C8,
        0x2881F3,
        0xC528F3,
        0xF3287B
    ]
    quotes = [
        "👀 This user has a lot of messages!",
        "😮 I'm impressed!",
        "💥 I can't handle that amount of messages!",
        "👏 Woah, you are really active!"
    ]
    messages = database_handler.returnValue("xp",str(user.id))
    firstmessage = database_handler.returnValue("first_message",str(user.id))
    level = database_handler.returnValue('level',str(user.id))
    message = []
    message.append(f'📈 Level: **{level}**\n🔢 XP: **{messages}** ([First message]({firstmessage}))\n\n')
    message.append(f'{random.choice(quotes)}\n')
    if level >= 70:
        message.append("🥇 This user got **all the available recompenses**!")
    elif level >= 50 and level <= 70:
        message.append("🏅 This user got **two of the available recompenses**!")
    elif level >= 30 and level <= 50:
        message.append("🥈 This user got only **one recompense**!")
    elif level <= 30:
        message.append('🥉 This user got **no recompenses**...yet!')
    embed = discord.Embed(
        color = random.choice(colors),
        title = f"🏆 {user.name}'s rank",
        description = ' '.join([str(elem) for elem in message])
    )    
    embed.set_author(
        name = user.name,icon_url=user.avatar_url
    )         
    await ctx.send(embed = embed)

@bot.command()
@has_permissions(manage_messages = True)
async def reset(ctx,user:discord.Member=None):
    if user != None:
        database_handler.modify(
            user.id, "xp",0
        )
        database_handler.modify(
            user.id, "level",0
        )
        database_handler.modify(
            user.id, "first_message",0
        )
        await ctx.send(f"Succesfully rested {user.mention}'s XP and levels.")
    else:
        await ctx.send('Error: missing an argument. You need to specify the user you want to reset the values of.')

# Commande pour reset valeur




## Level 30 => Reaction
## Level 50 => Custom color
## Level 70 => Free ECP (not shared) gave by devs if the user doesn't have ECP







bot.run("ODg3NzExMzE0NTkwNDM3NDM2.YUIHlg.yCD_P1UPvYBU8puleOlyQDXv-ec")