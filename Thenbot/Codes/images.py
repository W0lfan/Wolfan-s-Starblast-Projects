import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import random
import asyncio
from PIL import Image
import wikia

bot = commands.Bot(command_prefix = "c!")
bot.remove_command("help")
bot.remove_command("credits")




@bot.event
async def on_ready():
    print("Bot ready !")

@bot.event
async def on_message(message):
    TheMessage = message.content.split()
    for x in range(0,len(TheMessage)):
        if x == "panda":
            await ctx.send("nou")

@bot.command()
async def emoji(ctx, emoji:discord.Emoji):
    embed = discord.Embed(title=f"Emoji: '{emoji.name}'", description = f"Asked by {ctx.message.author.mention}")
    embed.set_image(url=emoji.url)
    embed.add_field(name="Link:", value=emoji.url)
    await ctx.send(embed=embed)

@bot.command()
async def pfp(ctx, user:discord.Member = None):
    if user == None:
        MessageAuthor = ctx.message.author
    elif user != None:
        MessageAuthor = user
    pfp = MessageAuthor.avatar_url
    embed = discord.Embed(title=f"{MessageAuthor.name}'s profile picture")
    embed.set_image(url=(pfp))
    await ctx.send(embed = embed)

@bot.command()
async def link(ctx, *name):
    message_content = " ".join(name)
    Name = str.lower(message_content)
    link = "https://starblastio.fandom.com/wiki/"
    NameLength = Name.split()
    if "-" in Name or len(NameLength) == 2:
        if "-" in Name:
            Name2 = Name.replace("-", " ")
            e = Name2.split()
        else:
            e = Name.split()
        NameFirstCapitalize = str.capitalize(e[0])
        NameSecondCapitalize = str.capitalize(e[1]) 
        await ctx.send(f"{link}{NameFirstCapitalize}-{NameSecondCapitalize}")
        return
    else:
        NameFirstCapitalize = str.capitalize(Name)
        await ctx.send(f"{link}{NameFirstCapitalize}")
        return

bot.run("") 
