import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import random
import asyncio



bot = commands.Bot(command_prefix = "c!")
bot.remove_command("help")
bot.remove_command("credits")




@bot.event
async def on_ready():
    print("Bot ready !")



@bot.command()
async def add(ctx, type, number):
    Type = str.lower(type)
    if Type == "options":
        options = [
            "station_size", "hues","station_regeneration", "station_crystal_capacity", "station_repair_treshold",
            "auto_assign_teams",
            "survival_time",
            "ships_groups",
            "root_mode", "reset_tree","ships","map_size","soundtrack","max_players","lives","max_level","friendly_colors",
            "map_name","survival_level","starting_ship","starting_ship_maxed","frictio_ratio","strafe","speed_mode",
            "rcs_toogle","map_id","map_density","weapon_drop","crystal_drop","release_crystals","mines_self_destroy",
            "mines_destroy_delay","healing_enabled","healing_ratio","shield_regen_factor","invulnerable_ships","weapons_store",
            "radar_zoom","auto_refill","projectile_speed","choose_ship","collider"
        ]
        optionsWithTrueOrFalse = ["auto_assign_teams","reset_tree","starting_ship_maxed","rcs_toogle",
            "mines_self_destroy","release_crystals","healing_enabled","auto_refill","collider","invulnerable_ships",
            "weapons_store"
        ]
        optionsWithArray = ["hues","ship_groups","choose_ship"]
        optionsWithNumber = [
            "station_size","station_regeneration","station_crystal_capacity","station_repair_treshold",
            "survival_time","map_size","max_players","lives","max_level","friendly_colors",
            "survival_level","starting_ship","frictio_ratio","strafe","speed_mode",
            "rcs_toogle","map_id","map_density","weapon_drop","crystal_drop","mines_destroy_delay",
            "healing_ratio","shield_regen_factor","radar_zoom","projectile_speed",""
        ]
        optionsWithMessages = [
            "root_mode","map_name"
        ]
        optionsWithNo = ["ships"]
        basicCode = [
        "this.options = {\n// see documentation for options reference\n","",
        '    root_mode: "survival",\n'+
        '    map_size: 30\n'+
        "};\n"
        ]

        def check(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel
        
        optionsToAdd = []
        valueDependingOnOptions = []
        for i in range(int(number)):
            await ctx.send(f"What option do you to want add? **(#{i+1})**")
            optionMessage = await bot.wait_for('message', timeout = 20, check = check)
            message = optionMessage.content
            noOptions = 0
            for option in options:
                if message != option:
                    noOptions = noOptions + 1
            if noOptions == len(options):
                await ctx.send(f'{ctx.message.author.mention} error, unknown option')
                return
            else:
                optionsToAdd.append(message)
            await ctx.send(f"What value do you want to add to this option? **(#{i+1})**")
            value = await bot.wait_for('message', timeout = 20, check = check)
            e = value.content
            valueDependingOnOptions.append(value.content)
        for e in range(int(number)):
            basicCode[1] = basicCode[1] + f"    {optionsToAdd[e]}:{valueDependingOnOptions[e]},\n"
        await ctx.send(f"```js\n{basicCode[0]}{basicCode[1]}{basicCode[2]}```")

@bot.command()
async def addTick(ctx, number, field, action:int):
    thisTick = [
        "this.tick = function(game) {\n",
        "}"
    ]
    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    await ctx.send(f"{ctx.message.author} do you want to add a tick part? (yes/no)")
    isTick = await bot.wait_for('message', timeout = 20, check = check)
    ISTick = str.lower(isTick.content)
    if ISTick == "no":
        await ctx.send(f"{ctx.message.author.mention} command canceled.")
        return
    elif ISTick == "yes":
        for i in range(action):
            await ctx.send(f"{ctx.message.author.mention} what tick do you want to add (number)?")
            e = await bot.wait_for('message', timeout = 20, check = check)
            whatTick = str.lower(e.content)
            if whatTick.isnumeric():
                last = thisTick[len(thisTick - 1)]
                thisTick.append(f"    if (game.step % {whatTick} == 0)" + "{\n\n    }\n")
                thisTick.append(last)
                await ctx.send(f"```js\n{thisTick[0]}{thisTick[1]}{thisTick[2]}```")





bot.run("") 
