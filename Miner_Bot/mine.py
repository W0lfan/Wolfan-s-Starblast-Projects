import discord
from discord import message
from discord.ext import commands, tasks
from discord.member import Member
import asyncio

class Mine:
    async def Mine(ctx,amount):
        maxINT = 0
        if amount:
            if amount <= 120:
                maxINT = amount
            elif amount > 120 or amount <= 0:
                embed = discord.Embed(
                    color = 0xE02525,
                    title = f"Error: you cannot mine {amount} gems. You are allowed to mine gems above 0 and under 120."
                )
                await ctx.send(ctx.message.author.mention,embed=embed)
            await ctx.send(f'**{ctx.message.author.mention}** Starting to mine, you will be pinged in {maxINT * 2} seconds.')
            embed = discord.Embed(
                color = 0x6A6A6A,
                title = f"{ctx.message.author.name}'s mining result",
                description = f"<:gem:878194858689458276> {ctx.message.author.mention} mined {maxINT} gems."
            )
            embed.set_footer(icon_url=ctx.message.author.avatar_url,text=ctx.message.author)
            await asyncio.sleep(maxINT * 2)
            await ctx.send(ctx.message.author.mention,embed=embed)