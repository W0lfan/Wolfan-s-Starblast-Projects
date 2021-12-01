import discord
from discord.ext import commands, tasks
import random
from random import randrange
import asyncio

bot = commands.Bot(command_prefix='+', case_insensitive = True)
bot.remove_command('help')
bot.remove_command('rules')



status = [
    "Starblast (+help)",
    'Starblast modding (+help)',
    'with pandas (+help)',
    'coding (+help)',
    ".gg/KRctjd4WjN (+help)"
]

@bot.event
async def on_message(message):
    channel = message.channel
    user = message.author
    if message.author.id != 772411699483115530 and message.author.id != 859152607200411679:
        if channel.name == "tests" or channel.name == "game-links":
            message_content = message.content
            messages = []
            z = []
            if (f'https://starblast.io/') in message_content:
                z = message_content.split()
                for x in z:
                    if 'https://starblast.io/' in x:
                        l = x.replace('https://starblast.io/','')
                        l = l.replace('#','')
                if not '@' in l and not ':' in l and not "." in l:
                    if l.isnumeric() != True:
                        messageToSend = [
                            f'{user.mention} please use correct game links: they must be a number (for example #20).\nYour message has been deleted and sent to you for your conveniance.'
                        ]
                        await message.delete()
                        await channel.send(messageToSend[0])
                        await user.send(message.content)
                    elif len(l) > 4 :
                        messageToSend = [
                            f'{user.mention} please use correct game links: they must be a number with less than 4 characters.\nYour message has been deleted and sent to you for your conveniance.'
                        ]
                        await channel.send(messageToSend[0])
                        await message.delete()
                        await channel.send()
                        await user.send(message.content)
                async for message_ in channel.history(limit = 11):
                    if message_.id != message.id:
                        message_content_ = message_.content
                        a = message_content_.split()
                        messageUsers = []
                        for i in a:
                            if 'https://starblast.io/#' in i:
                                o = i.replace('https://starblast.io/#','')
                                messages.append(o)
                                messageUsers.append(message_.author)
                        for i in messages:
                            if i == l:
                                iPos = messages.index(i)
                                messageToSend = [
                                    f'{user.mention} please do not repost a link that was already recently posted. `{messageUsers[iPos].name}` already posted a link to `https://starblast.io/#{i}`.\nYour message has been deleted and sent to you for your conveniance.'
                                ]
                                await message.delete()
                                await channel.send(messageToSend[0])
                                await user.send(message.content)
                                return
    for file in message.attachments:
        if file.filename.endswith((".exe", ".dll",".PNG")):
            await message.delete(f'{user.mention} please do not send executable files in this server. Sending executable files is considered as a potential issue and so is not allowed here.')
    await bot.process_commands(message)



@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(861979341336346637)
    channelWhereDelete = message.channel
    if channelWhereDelete.name == "tests" or channelWhereDelete.name == "starblast-media" or channelWhereDelete.name == "discord-invites" or channelWhereDelete.name == "game-links":
        if message.mentions:
            print("someone got mentionned")
            mention = []
            for i in message.mentions:
                mention.append(i.mention)
                print(i)
            listToStr = ', '.join([str(elem) for elem in mention])
            messageToSend = [
                f"{listToStr} you got mentionned by {message.author.mention} in #{channelWhereDelete.name} with message content: `{message.content}`."
            ]
            await channel.send(messageToSend[0])



@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(861979341336346637)
    channelWhereDelete = message.channel
    if channelWhereDelete.name == "tests" or channelWhereDelete.name == "starblast-media" or channelWhereDelete.name == "discord-invites" or channelWhereDelete.name == "game-links":
        if message.mentions:
            print("someone got mentionned")
            mention = []
            for i in message.mentions:
                mention.append(i.mention)
                print(i)
            listToStr = ', '.join([str(elem) for elem in mention])
            messageToSend = [
                f"{listToStr} you got mentionned by {message.author.mention} in #{channelWhereDelete.name} with message content: `{message.content}`."
            ]
            await channel.send(messageToSend[0])


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.send("Missing a required argument.")
        await asyncio.sleep(5)
        await message.delete()
    elif isinstance(error, commands.BotMissingPermissions):
        message = await ctx.send('You do not have the permissions to do that.')
        await asyncio.sleep(5)
        await message.delete()
    elif isinstance(error, commands.CommandInvokeError):
        message = await ctx.send(error)
        await asyncio.sleep(5)
        await message.delete()
    elif isinstance(error, commands.CommandNotFound):
        message = await ctx.send("This command does not exist.")
        await asyncio.sleep(5)
        await message.delete()
    elif isinstance(error, commands.TooManyArguments):
        message = await ctx.send("Too many arguments")
        await asyncio.sleep(5)
        await message.delete()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    statusBot.start()

@tasks.loop(hours = 2)
async def statusBot():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status = discord.Status.online, activity = game)

async def sendChat(user, command, server):
    staffLogsInfo = bot.get_channel(847905335955816460)
    embed=discord.Embed(title=f"Command used", description=f"Message sent from **{server}**", color=0xFFF93B)
    embed.add_field(name = "Command:", value = command, inline = False)
    embed.add_field(name = "User:", value = user, inline = False)
    await staffLogsInfo.send(embed = embed)


@bot.command()
async def suggestion(ctx,priority="no", *message):
    Priority = str.lower(priority)
    banned_userIDS = []
    for user in banned_userIDS:
        if ctx.message.author.id == user:
            await ctx.send("Error, you're banned from this command, you can't use it.")
            return
    message_content = " ".join(message)
    publicLogs = bot.get_channel(857214987813257236)
    user = ctx.message.author
    embed=discord.Embed(title=f"__Suggestion__", description=f"Message sent from **{ctx.guild.name}**", color=0x49FAD5)
    embed.set_author(name=f"{ctx.message.author}")
    embed.add_field(name = "Suggestion content:", value = message_content, inline = False)
    embed.add_field(name = "Suggestion author:", value = ctx.message.author.mention, inline = False)
    message = await publicLogs.send(embed = embed)
    await ctx.send(f"Thanks for your suggestion {ctx.message.author}!\nNote that any abuses of that command will result in a command ban.")
    await message.add_reaction("👍")
    await message.add_reaction("👎")
    await sendChat(ctx.message.author.mention, "suggestion",ctx.guild.name)
    list = [689452305212637253]
    for users in list:
        if ctx.message.author.id == users:
            if Priority == "yes":
                await message.pin()
                embed=discord.Embed(title=f"Pinned message from {ctx.guild.name}", description=f"Your suggestion from **{ctx.guild.name}** has been pinned in the support server because your ID is in the priority list.", color=0x49FAD5)
                embed.add_field(name = "Suggestion:", value = message_content, inline = False)
                await user.send(embed = embed)


@bot.command()
async def feedback(ctx, *message):
    banned_userIDS = []
    for user in banned_userIDS:
        if ctx.message.author.id == user:
            await ctx.send("Error, you're banned from this command, you can't use it.")
            return
        message_content = " ".join(message)
        publicLogs = bot.get_channel(857214987813257236)
        user = ctx.message.author
        embed=discord.Embed(title=f"__Feedback__", description=f"Message sent from **{ctx.guild.name}**", color=0xFFB128)
        embed.set_author(name=f"{ctx.message.author}")
        embed.add_field(name = "Feedback content:", value = message_content, inline = False)
        embed.add_field(name = "Feedback author:", value = ctx.message.author.mention, inline = False)
        await publicLogs.send(embed = embed)
        await ctx.send(f"Thanks for you Feedback {ctx.message.author.mention}!\nNote that any abuses of that command will result in a command ban.")
        await sendChat(ctx.message.author.mention, "feedback",ctx.guild.name)

@bot.command()
async def banID(ctx,  user:discord.Member = None, *reason ):
    if ctx.message.author.id == 689452305212637253:
        banChannel = bot.get_channel(857219561631383593)
        reason_content = " ".join(reason)
        embed=discord.Embed(title=f"__Ban logs__", description=f"Ban carried out from **{ctx.guild.name}**", color=0x1C1C1C)
        embed.set_author(name=f"{user}")
        embed.add_field(name = "Banned user:", value = f"{user.mention} (`{user.mention}`), {user}, {user.id}", inline = False)
        embed.add_field(name = "Reason", value = reason_content, inline = False)
        await ctx.send(f"Sucessfully sent {user.mention}'s informations to the ban list.")
        await banChannel.send(embed = embed)
        sendChat(ctx.message.author.mention, "ban",ctx.guild.name)

@bot.command()
async def ex(ctx, exType):
    exTypeReduced = str.lower(exType)
    if exTypeReduced == "ui":
        componentExample = [
            'var reset_button = {\n'
                + '     id: "reset",\n'
                + '     position: [5,30,8,14],\n'
                + '     clickable: true,\n'
                + '     shortcut: "R",\n'
                + '     visible: true,\n'
                + '     components: [\n'
                + '         { type: "box",position:[0,0,100,100],stroke:"#CDE",width:2},\n'
                + '         { type: "text",position:[10,35,80,30],value:"RESET",color:"#CDE"},\n'
                + '         { type: "text",position:[20,70,60,20],value:"[R]",color:"#CDE"}\n'
                + '     ]\n'
            +   '   };'
        ]
        embed = discord.Embed(color = 0x2833BF, title ="UI component example: UI", description = f"```js\n{componentExample[0]}```" )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/850081291101143070/850663555934060554/Capture.PNG")
        embed.add_field(name = "Full reset button link", value = "https://discord.com/channels/265400368765075456/741214091741364245/768158944899760188")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)
        await sendChat(ctx.message.author.mention, "ex ui",ctx.guild.name)
    elif exTypeReduced == "radar":
        componentExample = [
            'var radar_background = {\n'
                + '     id: "radar_background",\n'
                + '     components: [\n'
                + '         { type:"round",position:[40,39.5,20,20],fill:"#37E5A8",stroke:"#CDE",width:2},\n'
                + '         { type: "text",position:[42.5,42.5,15,15],value:"WARP",color:"#000000"},\n'
                + '     ]\n'
            +   '   };'
        ]
        embed = discord.Embed(color = 0x2833BF, title ="UI component example: radar background", description = f"```js\n{componentExample[0]}```" )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/850081291101143070/850662168671289344/Capture.PNG")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)
        await sendChat(ctx.message.author.mention, "ex radar",ctx.guild.name)
    elif exTypeReduced == "scoreboard":
        componentExample = [
            'var scoreboard = {\n'
                + '     id: "scoreboard",\n'
                + '     components: [\n'
                + '         { type: "text",position:[25,20,50,50],value:"WARP",color:"#CDE"},\n'
                + '     ]\n'
            +   '   };'
        ]
        embed = discord.Embed(color = 0x2833BF, title ="UI component example: radar background", description = f"```js\n{componentExample[0]}```" )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/850081291101143070/850662907376173076/Capture.PNG")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)
        await sendChat(ctx.message.author.mention, "ex scoreboard",ctx.guild.name)
    elif exTypeReduced == "3d":
        componentExample = [
            'var cube = {\n'
                + '     id: "cube",\n'
                + '     obj: "https://raw.githubusercontent.com/pmgl/starblast-modding/master/objects/cube/cube.obj",\n'
                + '     diffuse: "https://raw.githubusercontent.com/pmgl/starblast-modding/master/objects/cube/diffuse.jpg"\n'
            +   '   };'
            + "\n\n"
          + 'game.setObject({\n'
                + '     id: "cube",\n'
                + '     type: cube,\n'
                + '     position: { x:0,y:0,z:0 },\n'
                + '     rotation: { x:0,y:0,z:0 },\n'
                + '     scale: { x:1,y:1,z:1 }\n'
          + '});'

        ]
        embed = discord.Embed(color = 0x2833BF, title ="3D object code example", description = f"```js\n{componentExample[0]}```\n\nUse `game.removeObject(id)` to remove a 3D object from the game." )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/850081291101143070/850663888088465418/Capture.PNG")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)
        await sendChat(ctx.message.author.mention, "ex 3d",ctx.guild.name)
    elif exTypeReduced == 'vocabulary':
        vocabularyExample = [
        'var vocabulary = [\n'
        +'    { text: "Hello", icon:" \ u0045 ", key:"O" },\n'
        +'    { text: "Bye", icon:"\ u0046", key:"B" },\n'
        +'    { text: "Yes", icon:"\ u004c", key:"Y" },\n'
        +'    { text: "No", icon:"\ u004d", key:"N" },\n'

        +'    { text: "Flower", icon:"\ u{ 1F33B }", key:"F" },\n'
        +'    { text: "Snowman", icon:"\ u26c4", key:"M" },\n'
        +'    { text: "Shark", icon:"\ u{ 1F988 }", key:"S" },\n'
        +'    { text: "Ghost", icon:"\ u{ 1F47B }", key:"G" }\n'
        +'    ] ;'
        ]
        embed = discord.Embed(color = 0x2833BF, title ="Vocabulary code example", description = f"```js\n{vocabularyExample[0]}```\n\n(Remove the spaces in the 'icon' part)" )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "ex vocabulary",ctx.guild.name)
    elif exTypeReduced == 'intermissions':
        intermission = [
            'game.ships[0].intermission({ "Best Achievement" : "Managed to run the mod", "Score" : 1234})'
        ]
        gameover = [
            'game.ships[0].gameover({ "Rating":"Can do better","Score":1234})'
        ]
        embed = discord.Embed(color = 0x2833BF, title ="Intermissions & gameover code example", description = f"```js\n{intermission[0]}```\n\n```js\n{gameover[0]}```" )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "ex intermissions",ctx.guild.name)
    elif exTypeReduced == 'instructor':
        calling = [
            'ship.instructorSays("Hello!")\n//or\nship.instructorSays("Hello","Kan")\n//or\nship.showInstructor()'
        ]
        uncall = [
            'ship.hideInstructor()'
        ]
        embed = discord.Embed(color = 0x2833BF, 
        title ="Intermissions & gameover code example", 
        description = f"To call an instructor you can use```js\n{calling[0]}```\n\n```js\n{uncall[0]}```\n\nYou can see the available characters using `+pic character`." )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "ex instructor",ctx.guild.name)
    else:
        message = await ctx.send(f'{ctx.message.author.mention} unknown possible code. Please choose between `ui`, `radar`, `scorebard`, `3d`, `vocabulary`, `intermissions` or `instructor`.')
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "ex",ctx.guild.name)

@bot.command()
async def help(ctx):
        embedDesc = [
            "Bot prefix: `+`.\nI am a discord bot coded for help in starblast modding.\n"
            + "Commands takes a certain number of parameters.\n\n**__Available commands are:__**"
        ]
        embed = discord.Embed(
            color = 0x9CE16B,
            title = "**__Help page__**", 
            description = embedDesc[0]
            )
        embedField1FieldsInfos = [
            "Use `+info fields` to get access to an accessible field. Only `ships` field exists."
        ]
        embedFieldSet = [
            "Use `+info set` to get access to an accessible option to set an entity in modding."
            + "The accessible entities are `ships`, `aliens`, `asteroids`, `map` or `ui`."
        ]
        embedAddThings = [
            'Use `+info add` to add an entity in the game.'
            + "The entities you can add to the game are `aliens`, `asteroids` or `collectibles`. You can use `+aliens` to get access to all aliens codes"
        ]
        embedPictureAboutModding = [
            'Use `+pic` to see a related pic to modding.'
            + "To see a picture of starblast hues, use `hues`."
            + "To see a picture of one of the starblast characters, use `characters`."
        ]
        embedExamples = [
            'Use `+ex` to get access to different examples of starblast codes as `ui` components, `radar` background'
            + ' `scoreboard`, `3d`, `vocabulary`, `intermissions` or `instructor`.'
        ]
        embedOtherCommands = [
            'Use `+tools` to see the availables starblast tools.\nUse `+soundtrack` to listen to the available spotify soundtracks: `crystals`, `argon` or `procedurality`.'
        ]
        embedUtilities = [
            'Use `+utilities` to see the available useful codes and videos: `codes` or `videos`.'
        ]
        embedErrors = [
            'Use `+errors` to resolve errors you can possibly have while coding: `link` (no link appears), `crashes`, `mod stopped` or `latency`.'
        ]
        embedOptions = [
            'Use `+options` to see the available options in the different game modes as `team mode`, `survival mode`, `deathmatch`, `main`.'
        ]
        object3d = [
            'Use `+object3d` to see the available options for 3D objects: `type` or `instance`.'
        ]
        components = [
            'Use `+components` to see the available options for components and subcomponents: `main` or `sub`.'
        ]
        events  = [
            'Use `+events` informations related to game events: `code`, `ui code`, `examples`.'
        ]
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = 'Accessible fields in modding', value = embedField1FieldsInfos[0], inline = False)
        embed.add_field(name = 'Accessible options to set an entity in modding', value = embedFieldSet[0], inline = False)
        embed.add_field(name = 'Entities you can add in modding', value = embedAddThings[0], inline = False)
        embed.add_field(name = 'Pictures about modding', value = embedPictureAboutModding[0], inline = False)
        embed.add_field(name = 'This.options options', value = embedOptions[0], inline = False)
        embed.add_field(name = '3D objects options', value = object3d[0], inline = False)
        embed.add_field(name = 'Components and subcomponents options', value = components[0], inline = False)
        embed.add_field(name = 'Events examples and codes', value = events[0], inline = False)
        embed.add_field(name = 'Modding errors', value = embedErrors[0], inline = False)
        embed.add_field(name = 'Code examples', value = embedExamples[0], inline = False)
        embed.add_field(name = 'Code utilities', value = embedUtilities[0], inline = False)
        embed.add_field(name = 'Other commands', value = embedOtherCommands[0], inline = False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/823979651533635604/849688344051843082/thenpale.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "help",ctx.guild.name)



@bot.command()
async def add(ctx, type, number):
    def waitFor(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    await ctx.send(f"{ctx.message.author.mention}⚠️ **This feature is in beta. It is working but not 100% finished.**\nAre you sure you want to continue? (yes/no) ")
    confirmation = await bot.wait_for('message', timeout = 20, check = waitFor)
    Type = str.lower(type)
    if confirmation.content == "yes":
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
                basicCode[1] = basicCode[1] + f"    {optionsToAdd[e]}: {valueDependingOnOptions[e]},\n"
            await ctx.send(f"```js\n{basicCode[0]}{basicCode[1]}{basicCode[2]}```")
    else:
        await ctx.send(f"${ctx.message.author.mention} Command canceled.")
    await sendChat(ctx.message.author.mention, "options",ctx.guild.name)

@bot.command()
async def info(ctx, type, name):
    reducedName = str.lower(name)
    reducedType = str.lower(type)
    def waitEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji)== "➡️") 
            
            
    if reducedType == "field" or reducedType == "fields":
        if reducedName == "ships":
            await ctx.send(f"Available {reducedName}'s fields and options:")
            await sendChat(ctx.message.author.mention, "ships fields",ctx.guild.name)
            if reducedName == "ships":
                howToUse =  "\n**How to use it?**\nYou can use `ship.[FIELD]`, for example `ship.r` or `game.ships[ship_index].[FIELD]`, it'll return the corresponding value."
                embed = discord.Embed(
                    color = 0xCA44DA,
                    title = "**__Ships fields and options - 1__**", 
                    description = f"Asked by {ctx.message.author.mention}"
                )
                embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
                embed.add_field(name = 'x', value = "X ship's coordinate", inline = False)
                embed.add_field(name = 'y', value = "Y ship's coordinate", inline = False)
                embed.add_field(name = 'vx', value = "Velocity vector X component of the ship", inline = False)
                embed.add_field(name = 'vy', value = "Velocity vector Y component of the ship", inline = False)
                embed.add_field(name = 'r', value = "Ship rotation", inline = False)
                message = await ctx.send(embed = embed)
                await ctx.send(howToUse)
                await message.add_reaction("➡️")
                reaction, user = await bot.wait_for("reaction_add", timeout=10, check = waitEmoji)
                if reaction.emoji == "➡️":
                    await message.remove_reaction("➡️", ctx.message.author)
                    embed = discord.Embed(
                        color = 0xCA44DA,
                        title = "**__Ships fields and options - 2__**", 
                        description = f"Asked by {ctx.message.author.mention}"
                    )
                    embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
                    embed.add_field(name = 'name', value = "Ship name", inline = False)
                    embed.add_field(name = 'alive', value = "If the ship is alive or not", inline = False)
                    embed.add_field(name = 'type', value = "Tier and model of the ship", inline = False)
                    embed.add_field(name = 'stats', value = "How the stats of the ship are", inline = False)
                    embed.add_field(name = 'idle', value = "If the ship is in idle mode or not", inline = False)
                    await message.edit(embed=embed)
                    await message.add_reaction("➡️")
                    reaction, user = await bot.wait_for("reaction_add", timeout=10, check = waitEmoji)
                    if reaction.emoji == "➡️":
                        await message.remove_reaction("➡️", ctx.message.author)
                        embed = discord.Embed(
                            color = 0xCA44DA,
                            title = "**__Ships fields and options - 3__**", 
                            description = f"Asked by {ctx.message.author.mention}"
                        )
                        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
                        embed.add_field(name = 'team', value = "Ship's team", inline = False)
                        embed.add_field(name = 'score', value = "Ship's score", inline = False)
                        embed.add_field(name = 'shield', value = "Ship shield value", inline = False)
                        embed.add_field(name = 'generator', value = "Ship generator value", inline = False)
                        embed.add_field(name = 'crystals', value = "umber of crystals the ship has", inline = False)
                        embed.add_field(name = 'healing', value = "If the ship is in healing mode or not", inline = False)
                        await message.edit(embed=embed)
                        await message.remove_reaction("➡️", ctx.message.author)
        elif reducedName != "ships":
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"{ctx.message.author.mention}, unknown accessible field, be sure to send a correct one (ships, aliens or asteroids).")
            await asyncio.sleep(10)
            await message.delete()
    if reducedType == "set":
        if reducedName == "ui":
            await ctx.send(
                'You can set an UI component for a ship with `ship.setUIComponent(COMPONENT NAME)`.\n'
                + "You can set an UI component for a specific ship with `game.ships[SHIP ID].setUIComponent(COMPONENT NAME)`."
            )
            await sendChat(ctx.message.author.mention, "set ui",ctx.guild.name)
        elif reducedName == "map":
            await ctx.send("Here is how to set a custom map when the game is running:")
            setMap = [
                "game.setCustomMap(<map pattern>)"
            ]
            await ctx.send(f"```js\n{setMap[0]}```")
            await sendChat(ctx.message.author.mention, "set map",ctx.guild.name)
        elif reducedName == "ships":
            embed = discord.Embed(
                color = 0xCA44DA,
                title = "**__Ships options usable with ship.set - 1__**", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.add_field(name = 'x', value = "Set ship coordinate (x)", inline = False)
            embed.add_field(name = 'y', value = "Set ship coordinate (y)", inline = False)
            embed.add_field(name = 'vx', value = "Set ship Velocity vector X component (vx)", inline = False)
            embed.add_field(name = 'vy', value = "Set ship Velocity vector X component (vy)", inline = False)
            embed.add_field(name = 'unvulnerable', value = "Set the ship to invulnerable (in ticks, 60 ticks = 1 second)", inline = False)
            embed.add_field(name = 'type', value = "Set ship type (tier * 100 + model)", inline = False)
            embed.add_field(name = 'angle', value = "Set ship angle", inline = False)
            embed.add_field(name = 'score', value = "Set ship score", inline = False)
            embed.add_field(name = 'idle', value = "Set ship to idle mode/to normal mode (idle means that the ship can't move and shoot anymore", inline = False)
            howToUseSetShips =  "\n**How to use it?**\nYou can use `ship.set({ [OPTIONS] })`, for example `ship.set({ type: 101 })` or `game.ships[ship_index].set({ [OPTIONS] })`. You can add multiples options at the same time, as `ship.set({type:101,crystals:10, ETC})`."
            message = await ctx.send(embed = embed)
            await sendChat(ctx.message.author.mention, "set ships",ctx.guild.name)
            await ctx.send(howToUseSetShips)
            await message.add_reaction("➡️")
            reaction, user = await bot.wait_for("reaction_add", timeout=10, check = waitEmoji)
            if reaction.emoji == "➡️":
                embed = discord.Embed(
                    color = 0xCA44DA,
                    title = "**__Ships options usable with ship.set - 2__**", 
                    description = f"Asked by {ctx.message.author.mention}"
                )
                embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
                embed.add_field(name = 'shield', value = "Set ship shield value (value/ship shield max value)", inline = False)
                embed.add_field(name = 'generator', value = "Set ship generator (value/ship generator max value)", inline = False)
                embed.add_field(name = 'healing', value = "Enable healing for the ship/disable it (true/false)", inline = False)
                embed.add_field(name = 'crystals', value = "Set ship crystals", inline = False)
                embed.add_field(name = 'stats', value = "Set ship stats (8 stats, like 11111111, maximum allowed number per stat has to be: max < ship tier)", inline = False)
                embed.add_field(name = 'kill', value = "Kill the ship (true)", inline = False)
                embed.add_field(name = 'team', value = "Set ship team (between 0 and X where x = number of teams - 1)", inline = False)
                embed.add_field(name = 'collider', value = "Enable or disable ship's collider (disable collisions/enable, etc) (true/false)", inline = False)
                embed.add_field(name = 'hue', value = "Set ship hue", inline = False)
                await message.edit(embed=embed)
                await message.remove_reaction("➡️", ctx.message.author)
        elif reducedName == "aliens":
                await ctx.send(f"Available options to set an alien:")
                howToUseAlienSet =  "\n**How to use it?**\nYou can use `alien.set({ [OPTIONS] })`, for example `alien.set({ kill: true })` or `game.aliens[Alien_id].set({ [OPTIONS] })`. You can add multiples options at the same time, as `alien.set({kill:true,rate:10, ETC})`."
                embed = discord.Embed(
                    color = 0xCA44DA,
                    title = "**__Aliens options usable with alien.set__**", 
                    description = f"Asked by {ctx.message.author.mention}"
                )
                embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
                embed.add_field(name = 'x', value = "Set alien coordinate (x)", inline = False)
                embed.add_field(name = 'y', value = "Set alien coordinate (y)", inline = False)
                embed.add_field(name = 'vx', value = "Set alien Velocity vector X component (vx)", inline = False)
                embed.add_field(name = 'vy', value = "Set alien Velocity vector X component (vy)", inline = False)
                embed.add_field(name = 'shield', value = "Set alien shield value", inline = False)
                embed.add_field(name = 'regen', value = "Set alien shield regen value", inline = False)
                embed.add_field(name = 'damage', value = "Set alien laser damage", inline = False)
                embed.add_field(name = 'laser_speed', value = "Set alien laser speed", inline = False)
                embed.add_field(name = 'rate', value = "Set alien laser rate (number of shots per seconds)", inline = False)
                embed.add_field(name = 'kill', value = "Kill an alien (true)", inline = False)
                await ctx.send(embed = embed)
                await ctx.send(howToUseAlienSet)
                await sendChat(ctx.message.author.mention, "set aliens",ctx.guild.name)
        elif reducedName == "asteroids":
                await ctx.send(f"Available options to set an asteroid:")
                howToUseAsteroidsSet =  "\n**How to use it?**\nYou can use `asteroid.set({ [OPTIONS] })`, for example `asteroid.set({ kill: true })` or `game.asteroids[Asteroid_id].set({ [OPTIONS] })`. You can add multiples options at the same time, as `asteroid.set({kill:true,size:64, ETC})`."
                embed = discord.Embed(
                    color = 0xCA44DA,
                    title = "**__Asteroids options usable with asteroid.set__**", 
                    description = f"Asked by {ctx.message.author.mention}"
                )
                embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
                embed.add_field(name = 'x', value = "Set asteroid coordinate (x)", inline = False)
                embed.add_field(name = 'y', value = "Set asteroid coordinate (y)", inline = False)
                embed.add_field(name = 'vx', value = "Set asteroid Velocity vector X component (vx)", inline = False)
                embed.add_field(name = 'vy', value = "Set asteroid Velocity vector X component (vy)", inline = False)
                embed.add_field(name = 'size', value = "Set asteroid size from 1 to 100", inline = False)
                embed.add_field(name = 'kill', value = "Kill an asteroid (true)", inline = False)
                await ctx.send(embed = embed)
                await ctx.send(howToUseAsteroidsSet)
                await sendChat(ctx.message.author.mention, "set asteroids",ctx.guild.name)
        elif reducedType != "ships" and reducedType != "aliens" and reducedType != "asteroids":
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"{ctx.message.author.mention}, unknown field to set, be sure to send a correct one (ships, aliens or asteroids).")
            await asyncio.sleep(10)
            await message.delete()
            await sendChat(ctx.message.author.mention, "set",ctx.guild.name)
    if reducedType == "add":
        if reducedName == "alien" or reducedName == "aliens":
            embed = discord.Embed(
                color = 0xDA445B,
                title = "**__game.addAlien__**", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.add_field(name = 'x', value = "Set alien coordinate (x)", inline = False)
            embed.add_field(name = 'y', value = "Set alien coordinate (y)", inline = False)
            embed.add_field(name = 'vx', value = "Set alien Velocity vector X component (vx)", inline = False)
            embed.add_field(name = 'vy', value = "Set alien Velocity vector X component (vy)", inline = False)
            embed.add_field(name = 'code', value = "Set alien code", inline = False)
            embed.add_field(name = 'level', value = "Set alien level", inline = False)
            embed.add_field(name = 'points', value = "Set the number of points the alien will give when being killed", inline = False)
            embed.add_field(name = 'crystal_drop', value = "Set the number of crystals the alien will give when being killed", inline = False)
            embed.add_field(name = 'weapon_drop', value = "Set the weapon the alien will give when being killed", inline = False)
            await ctx.send(embed = embed)
            await ctx.send('You have to use `game.addAlien({ OPTIONS })`\nNote that you are not obligated to put some options. If you do not put some of them they will be automatically put with an automatic value.')
            await sendChat(ctx.message.author.mention, "add aliens",ctx.guild.name)
        elif reducedName == "asteroids" or reducedName == "asteroid":
            embed = discord.Embed(
                color = 0xDA445B,
                title = "**__Asteroids options usable with asteroid.set__**", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.add_field(name = 'x', value = "Set asteroid coordinate (x)", inline = False)
            embed.add_field(name = 'y', value = "Set asteroid coordinate (y)", inline = False)
            embed.add_field(name = 'vx', value = "Set asteroid Velocity vector X component (vx)", inline = False)
            embed.add_field(name = 'vy', value = "Set asteroid Velocity vector X component (vy)", inline = False)
            embed.add_field(name = 'size', value = "Set asteroid size from 1 to 100", inline = False)
            await ctx.send(embed = embed)
            await ctx.send('You have to use `game.addAsteroid({ OPTIONS })`\nNote that you are not obligated to put some options. If you do not put some of them they will be automatically put with an automatic value.')
            await sendChat(ctx.message.author.mention, "add asteroids",ctx.guild.name)
        elif reducedName == "collectible" or reducedName == "collectibles":
            howToAddCollectible = [
                "To create a collectible you have to write `game.addCollectible({ code: collectible code, x: x position, y: y position})`."
                + "\nReact with 🔵 to get access to colectibles codes.\n\nNote: you can remove all the secondaries of a ship using `ship.emptyWeapons()`."
            ]
            message = await ctx.send(howToAddCollectible[0])
            await message.add_reaction("🔵")

            def waitEmoji1(reaction, user):
                return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji)== "🔵") 
            
            await sendChat(ctx.message.author.mention, "add collectibles",ctx.guild.name)
            reaction, user = await bot.wait_for("reaction_add", timeout=10, check = waitEmoji1)
            if reaction.emoji == "🔵":
                embed = discord.Embed(
                    color = 0xDA445B,
                    title = "**__Collectibles codes__**", 
                    description = f"Asked by {ctx.message.author.mention}"
                )
                embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
                embed.add_field(name = '10', value = "4 rockets pack", inline = True)
                embed.add_field(name = '11', value = "2 missiles pack", inline = True)
                embed.add_field(name = '12', value = "1 toperdo", inline = True)
                embed.add_field(name = '20', value = "8 light mines pack", inline = True)
                embed.add_field(name = '21', value = "4 heavy mines pack", inline = True)
                embed.add_field(name = '40', value = "1 mining pod", inline = True)
                embed.add_field(name = '41', value = "1 attack pod", inline = True)
                embed.add_field(name = '42', value = "1 defense pod", inline = True)
                embed.add_field(name = '90', value = "1 energy refill battery", inline = True)
                embed.add_field(name = '90', value = "1 shield refill battery", inline = True)
                await message.edit(embed = embed)
                await message.remove_reaction("🔵", ctx.message.author)

@bot.command()
async def aliens(ctx):
    embed = discord.Embed(
        color = 0xDA445B,
        title = "**__Aliens codes__**", 
        description = f"Asked by {ctx.message.author.mention}"
    )
    embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
    embed.add_field(name = '10', value = "Chicken", inline = True)
    embed.add_field(name = '11', value = "Crab", inline = True)
    embed.add_field(name = '12', value = "Fortress", inline = True)
    embed.add_field(name = '13', value = "Some weird new thingy", inline = True)
    embed.add_field(name = '14', value = "Candlestick", inline = True)
    embed.add_field(name = '15', value = "Hirsute", inline = True)
    embed.add_field(name = '16', value = "Piranha", inline = True)
    embed.add_field(name = '17', value = "Pointu", inline = True)
    embed.add_field(name = '18', value = "Fork", inline = True)
    embed.add_field(name = '19', value = "Saucer", inline = True)
    embed.add_field(name = '20', value = "Final boss", inline = True)
    await ctx.send(embed = embed)
    await sendChat(ctx.message.author.mention, "aliens",ctx.guild.name)

@bot.command()
async def errors(ctx, *type):
    message_content = " ".join(type)
    Type = str.lower(message_content)

    if Type == "black screen":
        embed = discord.Embed(
            color = 0x482AB4,
            title = "**__Starblast modding common errors: black screen__**", 
            description = f"Asked by {ctx.message.author.mention}"
        )
        embed.add_field(name = '1. Ship tree', value = 'Your ship tree **has** to have a tier 1.'
        + "\nAlso, if you have tier 2 ships, you **must** have a tier 1 ship."
        , inline = True)
        embed.add_field(
            name = '2. Ships models', 
            value = 'Ships models are supposed to go in the right order: 1,2,3; not 1,5,9.'
            + "\nHowever, you can use `next` parameter to control ships paths. "
            + "When using it, be sure it ends at some ship, routes can't come back to a ship.",
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "errors black screen",ctx.guild.name)
    elif Type == "crashes":
        embed = discord.Embed(
            color = 0x482AB4,
            title = "**__Starblast modding common errors: mod crashes__**", 
            description = f"Asked by {ctx.message.author.mention}"
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = '1. Reloads', value = 'You reloaded or closed the page without ending the mod.', inline = True)
        embed.add_field(name = '2. Connection', value = 'Your connection is instable.', inline = False)
        embed.add_field(name = '3. Server error', value = 'Server has an error, it automatically disconnect the controller by itself.', inline = False)
        embed.add_field(name = '4. Browser', value = 'Your browser can crash because of some codes.', inline = False)
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "errors crashes",ctx.guild.name)
    elif Type == "link":
        embed = discord.Embed(
            color = 0x482AB4,
            title = "**__Starblast modding common errors: link do not appear__**", 
            description = f"Asked by {ctx.message.author.mention}"
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = '1. Connection', value = 'Bad connection can be a consequence of a non-appearing link.', inline = True)
        embed.add_field(name = '2. Code', value = 'Code can have errors / be really heavy.', inline = False)
        embed.add_field(name = '3. Modding link', value = "The link you're on is maybe [this one](https://starblast.data.neuronality.com/modding/moddingcontent.html#)"
        + ", it is a wrong link. Be sure that you're on [this link](https://starblast.io/modding.html)."
        , inline = False)
        await ctx.send(embed=embed)
        await sendChat(ctx.message.author.mention, "errors link ",ctx.guild.name)
    elif Type == "latency":
        embed = discord.Embed(
            color = 0x482AB4,
            title = "**__Starblast modding common errors: mod latency__**", 
            description = f"Asked by {ctx.message.author.mention}"
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = '1. Connection', value = 'Bad connection make the mod having an high latency.', inline = True)
        embed.add_field(name = '2. Tab', value = 'Always keep modding tab active when hosting this mod owerthise you will get issues in the game:', inline = False)
        embed.set_image(url = "https://camo.githubusercontent.com/3591976938de59686da11b949e4bde5627dc39907fe81214578f5da79da68848/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3833333338343139333236323232333339322f3834353333363434383438333332383032302f436170747572652e504e47")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "errors latency",ctx.guild.name)
    else:
        message = await ctx.send(f'{ctx.message.author.mention} unknown error. Please send an error between `black screen`, `crashes`, `link` or `latency`.')
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "errors",ctx.guild.name)

@bot.command()
async def pic(ctx, type):
    reducedType = str.lower(type)

    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    if reducedType == "hues" or reducedType == "hue":
        embed = discord.Embed(
            color = 0xDE70E8,
            title = " ", 
            description = f"Asked by {ctx.message.author.mention}"
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.set_image(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/b/bf/Hues_ruler.png/revision/latest/scale-to-width-down/500?cb=20210124185008")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "pic hues ",ctx.guild.name)
    elif reducedType == "characters" or reducedType == "character":
        await ctx.send('What character do you want the picture of?\n(Lucina, Klaus, Maria, Kan, Zoltar)')
        character = await bot.wait_for("message", timeout = 10, check = checkMessage)
        reducdedCharacter = str.lower(character.content) 
        if reducdedCharacter == "lucina":
            embed = discord.Embed(
                color = 0xDE70E8,
                title = " ", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.set_image(url="https://camo.githubusercontent.com/2f09b1d5d0730f99e4fc45c1e6d158d9f5a6ca4070778c3b158ca9027b3d3ee9/68747470733a2f2f73746172626c6173742e646174612e6e6575726f6e616c6974792e636f6d2f696d672f7475746f7269616c2d737572766976616c2e706e67")
            await ctx.send(embed = embed)
            await sendChat(ctx.message.author.mention, "pic lucina ",ctx.guild.name)
        elif reducdedCharacter == "klaus":
            embed = discord.Embed(
                color = 0xDE70E8,
                title = " ", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.set_image(url="https://camo.githubusercontent.com/123ec9ba4c9784c48ab667e62f708464937530e8a17c860299054aa4c45ce45e/68747470733a2f2f73746172626c6173742e646174612e6e6575726f6e616c6974792e636f6d2f696d672f7475746f7269616c2d626174746c65726f79616c652e706e67")
            await ctx.send(embed = embed)
            await sendChat(ctx.message.author.mention, "pic klaus ",ctx.guild.name)
        elif reducdedCharacter == "maria":
            embed = discord.Embed(
                color = 0xDE70E8,
                title = " ", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.set_image(url="https://camo.githubusercontent.com/ace841f73efe1c58f9dd0654ec9a9cc9d1e903b30b7492dd3067f48fd75a8371/68747470733a2f2f73746172626c6173742e646174612e6e6575726f6e616c6974792e636f6d2f696d672f7475746f7269616c2d7465616d2e706e67")
            await ctx.send(embed = embed)
            await sendChat(ctx.message.author.mention, "pic maria ",ctx.guild.name)
        elif reducdedCharacter == "kan":
            embed = discord.Embed(
                color = 0xDE70E8,
                title = " ", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.set_image(url="https://camo.githubusercontent.com/5d6b25dac5cf60cfe2f9220350d19f60503f4ef4286701debd3726576d216768/68747470733a2f2f73746172626c6173742e646174612e6e6575726f6e616c6974792e636f6d2f696d672f7475746f7269616c2d696e766173696f6e2e706e67")
            await ctx.send(embed = embed)
            await sendChat(ctx.message.author.mention, "pic kan ",ctx.guild.name)
        elif reducdedCharacter == "zoltar":
            embed = discord.Embed(
                color = 0xDE70E8,
                title = " ", 
                description = f"Asked by {ctx.message.author.mention}"
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            embed.set_image(url="https://camo.githubusercontent.com/86d10cd6b410d3553be2e1eebce2c826f603ea73cd611666cc8a51a53107c5d1/68747470733a2f2f73746172626c6173742e646174612e6e6575726f6e616c6974792e636f6d2f696d672f7475746f7269616c2d64656174686d617463682e706e67")
            await ctx.send(embed = embed)
            await sendChat(ctx.message.author.mention, "pic zoltar ",ctx.guild.name)
        elif reducdedCharacter != "lucina" and reducdedCharacter != "klaus" and reducdedCharacter != "maria" and reducdedCharacter != "kan" and reducdedCharacter != "zoltar":
            message = await ctx.send(f"{ctx.message.author.mention} unknown character, please send a name between these names: Lucina, Klaus, Maria, Kan or Zoltar. \nType to command again to try again.")
            await asyncio.sleep(10)
            await message.delete()
            await sendChat(ctx.message.author.mention, "pic",ctx.guild.name)

@bot.command()
async def tools(ctx):
    embed = discord.Embed(
        color = 0x9CE16B,
        title = "**__Available starblast modding tools__**", 
        description = f"Asked by {ctx.message.author.mention}"
    )
    embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
    embed.add_field(name = 'Starblast ship editor', value = 'Click [here](https://starblast.io/shipeditor/)', inline = True)
    embed.add_field(name = 'Starblast mod editor', value = 'Click [here](https://starblast.io/modding.html)', inline = True)
    embed.add_field(name = 'Starblast icons (vocabulary)', value = 'Click [here](https://starblast.io/glyphs.html)', inline = True)
    embed.add_field(name = 'SET', value = 'Click [here](https://chrome.google.com/webstore/detail/starblast-enhancement-too/bidhmieomigmdphceifkifanapkgmplc)', inline = True)
    embed.add_field(name = 'Starblast map editor', value = 'Click [here](https://bhpsngum.github.io/starblast/mapeditor/)', inline = True)
    embed.add_field(name = 'Starblast mod archives', value = 'Click [here](https://bhpsngum.github.io/starblast/mods/)', inline = True)
    embed.add_field(name = 'Starblast ship code converter', value = 'Click [here](https://bhpsngum.github.io/starblast/sscv/)', inline = True)
    embed.add_field(name = 'Javascript docs', value =  '[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)', inline = True)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/765972969540419636/850656441210634240/download.png")
    await ctx.send(embed = embed)
    await sendChat(ctx.message.author.mention, "tools",ctx.guild.name)

@bot.command()
async def utilities(ctx):
    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    await ctx.send(f"{ctx.message.author.mention} what type of utilities do you want?\nYou can choose between `videos` or `codes`.")

    e = await bot.wait_for("message", timeout = 10, check = checkMessage)
    typeOfUtilities = str.lower(e.content)
    if typeOfUtilities == "video" or typeOfUtilities == "videos":
        embed = discord.Embed(
            color = 0xE5E870,
            title = "**__Starblast modding useful videos__**", 
            description = f"Asked by {ctx.message.author.mention}"
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = 'Starblast general modding videos', value = 'By [Wolfan](https://www.youtube.com/watch?v=35SM5rFteIs)', inline = True)
        embed.add_field(name = 'Starblast ship editing videos', value = 'By [ATK](https://www.youtube.com/watch?v=r916KbgQ82w)', inline = True)
        embed.add_field(name = 'Starblast adding a ship into a game', value = 'By [Interdictor](https://www.youtube.com/watch?v=3b2zKArOkXk)', inline = True)
        embed.add_field(name = 'Starblast adding background objects into a game', value = 'By [Interdictor](https://www.youtube.com/watch?v=waT0qT6nxo8)', inline = True)
        embed.add_field(name = 'Starblast "How to use SET"', value = 'By [Bhpsngum](https://www.youtube.com/watch?v=ptsPT5CF2MU)', inline = True)
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "tools videos",ctx.guild.name)
    elif typeOfUtilities == "code" or typeOfUtilities == "codes":
        embed = discord.Embed(
            color = 0xE5E870,
            title = "**__Starblast codes examples and mods__**", 
            description = f"Asked by {ctx.message.author.mention}"
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = 'Starblast mods archives', value = 'By [Bhpsngum](https://bhpsngum.github.io/starblast/mods/)', inline = True)
        embed.add_field(name = 'Starblast codes snippets', value = 'By [Wolfan](https://github.com/W0lfan/Starblast-code-snippets)', inline = True)
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "codes",ctx.guild.name)
    else:
        message = await ctx.send(f"{ctx.message.author.mention} unknown utility. Please choose between `videos` or `codes`.")
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "tools",ctx.guild.name)

@bot.command()
@commands.has_permissions(manage_messages = True)
async def say(ctx, channel_e: int, *text):
    channel = bot.get_channel(channel_e)
    message_content = " ".join(text)
    await channel.send(message_content)

@bot.command()
async def events(ctx, *eventType):
    message_content = " ".join(eventType)
    eventType_ = str.lower(message_content)
    if eventType_ == 'code':
        eventMain = [
        '  this.event = function(event,game) {\n'
        +'  switch (event.name) {\n'
        +'    case "ship_spawned":\n'
        +'      if (event.ship != null) {\n'
        +'        shipJustSpawned(event.ship) ;\n'
        +'      }\n'
        +'      break ;\n'
        +'   }\n'
        +' };\n'
        ]
        embed = discord.Embed(color = 0x2833BF, title ="Main this.event code", description = f"```js\n{eventMain[0]}```" )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)
        await sendChat(ctx.message.author.mention, "events code",ctx.guild.name)
    elif eventType_ == "ui code":
        eventUICode = [
        'this.event = function(event,game) {\n'
        +'switch (event.name) {\n'
        +'    case "ui_component_clicked":\n'
        +'    var ship = event.ship ;\n'
        +'    var component = event.id ;\n'
        + '    if (component == "Component ID") {\n'
        +'        //action\n'
        +'     }'
        +'    break ;\n'
        +'   }\n'
        +'} ;\n'
        ]
        embed = discord.Embed(color = 0x2833BF, title ="Main this.event code", description = f"```js\n{eventUICode[0]}```" )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        embed.add_field(name = "Asked by:", value = f"{ctx.message.author.mention}")
        await ctx.send(embed=embed)
        await sendChat(ctx.message.author.mention, "events ui",ctx.guild.name)
    elif eventType_ == "examples":
        embed = discord.Embed(color = 0x2833BF, title ="Events examples", description = "" )
        embed.add_field(
            name = 'ship_spawned',
            value = 'A ship just spawned in game or respawned (`event.ship`)',
            inline = False
        )
        embed.add_field(
            name = 'ship_destroyed',
            value = 'A ship was just destroyed (`event.ship`, `event.killer`)',
            inline = False
        )
        embed.add_field(
            name = 'alien_destroyed',
            value = 'An alien was just killed (`event.alien`, `event.killer`)',
            inline = False
        )    
        embed.add_field(
            name = 'asteroid_destroyed',
            value = "A movable asteroid was just destroyed (this event won't trigeger for non-movable asteroids) (`event.asteroid`, `event.killer`)",
            inline = False
        )
        embed.add_field(
            name = 'collectible_picked',
            value = 'A ship just picked a collectible item (`event.collectible`, `event.ship`)',
            inline = False
        )
        embed.add_field(
            name = 'Ship disconnected',
            value = 'A ship was just disconnected: [code](https://raw.githubusercontent.com/Bhpsngum/starblast/master/ship_disconnected_event.js)',
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "events examples (list)",ctx.guild.name)
    else:
        message = await ctx.send(f"{ctx.message.author.mention} unknown event argument. Please choose an argument between `code`, `ui code` or `examples`.")
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "events",ctx.guild.name)

@bot.command()
async def components(ctx, type):
    reducedType = str.lower(type)
    if reducedType == "main":
        embed = discord.Embed(color = 0x2DC863, title ="Components main options", description = "" )
        embed.add_field(
            name = "id",
            value = "A unique identifier for this component, mandatory",
            inline = False
        )
        embed.add_field(
            name = "position",
            value = "Expressed in percentage of the main screen, the position of the component [x,y,width,height]. Example: [45,45,10,10] creates a component in the center of the screen, which width and height are 10 percent of the screen width and height.	",
            inline = False
        )
        embed.add_field(
            name = "visible",
            value = "Whether the component is visible or not. Resend the same data with visible set to false to hide the component	",
            inline = False
        )
        embed.add_field(
            name = "clickable",
            value = "Whether this component can be clicked or not",
            inline = False
        )
        embed.add_field(
            name = "shortcut",
            value = "When the component is clickable, a keyboard shortcut allowing to trigger the click event	",
            inline = False
        )
        embed.add_field(
            name = "components",
            value = "Gives a list (array) of graphical features to render within the component, which will be described with `+components sub`.",
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "main",ctx.guild.name)
    elif reducedType == "sub":
        embed = discord.Embed(color = 0x2DC863, title ="Subcomponents main options", description = "" )
        embed.add_field(
            name = "type",
            value = 'Type of the subcomponent. Currently supported: "round”, "text”, "box” or "player”',
            inline = False
        )
        embed.add_field(
            name = "id ('player' type only)",
            value = 'Id of the player associated with the subcomponent, which will be disapleyd as their name and badge (if exists) in the rendered subcomponent	”',
            inline = False
        )
        embed.add_field(
            name = "position",
            value = 'Positions of the subcomponent, formatted as [x,y,width,height]. That subcomponent are meant within the main component coordinates',
            inline = False
        )
        embed.add_field(
            name = "value",
            value = 'Value of the subcomponent, e.g value:"Sample text"	',
            inline = False
        )
        embed.add_field(
            name = "color",
            value = 'Text color of the subcomponent, this can be a string with any color formats (hex, hsla, rgb, etc.), e.g "#fff"	',
            inline = False
        )
        embed.add_field(
            name = "fill",
            value = 'Background color of the subcomponent, same format as the color property',
            inline = False
        )
        embed.add_field(
            name = "width",
            value = 'Width of the subcomponent’s border (in percent)',
            inline = False
        )
        embed.add_field(
            name = "stroke",
            value = 'Border color of the subcomponent, same format as the color property',
            inline = False
        )
        embed.add_field(
            name = "align",
            value = 'Alignment of the texts inside the subcomponent. "left”, "right” or "center” only',
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "sub",ctx.guild.name)
    else:
        message = await ctx.send(f"{ctx.message.author.mention} unknown component option. Please choose between `main` or `sub`.")
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "components",ctx.guild.name)


@bot.command()
async def object3d(ctx, type):
    reducedType = str.lower(type)
    if reducedType == 'type':
        embed = discord.Embed(color = 0x2DADC6, title ="Object type options", description = f"Asked by {ctx.message.author.mention}" )
        embed.add_field(
            name = "id",
            value = 'A unique identifier for this object type, mandatory',
            inline = False
        )
        embed.add_field(
            name = "obj",
            value = 'A URL to the OBJ file',
            inline = False
        )
        embed.add_field(
            name = "type",
            value = 'Object instance options, see the section below for more details',
            inline = False
        )
        embed.add_field(
            name = "diffuse",
            value = 'A URL to a diffuse texture file (optional)',
            inline = False
        )
        embed.add_field(
            name = "emissive",
            value = 'A URL to an emissive texture file (optional)',
            inline = False
        )
        embed.add_field(
            name = "specular",
            value = 'A URL to a specularity texture file (optional)',
            inline = False
        )
        embed.add_field(
            name = "bump",
            value = 'A URL to a bump texture map (optional)',
            inline = False
        )
        embed.add_field(
            name = "diffuseColor",
            value = 'Diffuse color of the object, e.g. 0xFF0000 (for red)',
            inline = False
        )
        embed.add_field(
            name = "emissiveColor",
            value = 'Emissive color of the object, e.g. 0x00FF00 (for green)',
            inline = False
        )
        embed.add_field(
            name = "specularColor",
            value = 'Specular color of the object, e.g. 0x0000FF (for blue)',
            inline = False
        )
        embed.add_field(
            name = "transparent",
            value = 'Whether the object’s texture has transparency or not',
            inline = False
        )
        embed.add_field(
            name = "bumpScale",
            value = 'Scale for bump mapping (default: 0.1)',
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "object3d type",ctx.guild.name)
    elif reducedType == "instance":
        embed = discord.Embed(color = 0x2DADC6, title ="Object instance options", description = f"Asked by {ctx.message.author.mention}" )
        embed.add_field(
            name = "id",
            value = 'A unique identifier for this object instance (mandatory, allows changing the object afterwards)',
            inline = False
        )
        embed.add_field(
            name = "type",
            value = 'The object type definition',
            inline = False
        )
        embed.add_field(
            name = "position",
            value = 'Coordinates for placing the object',
            inline = False
        )
        embed.add_field(
            name = "scale",
            value = 'Allows to scale the object',
            inline = False
        )
        embed.add_field(
            name = "rotation",
            value = 'Allows to rotate the object',
            inline = False
        )
        embed.add_field(
            name = "shape",
            value = 'Object’s shape (used for creating hitbox).\nNote: We recommend not to use this property as it usually doesn’t work as expected',
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "object3d isntance",ctx.guild.name)
    else:
        message = await ctx.send(f"{ctx.message.author.mention} unknown object option. Please choose between `type` or `instance`.")
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "object3d",ctx.guild.name)

@bot.command()
async def options(ctx, optionsType):
    optionsType_ = str.lower(optionsType)
    if optionsType_ == "team mode" or optionsType_ == "team":
        embed = discord.Embed(color = 0xDA7B44, title ="Team mode this.options options", description = f"Asked by {ctx.message.author.mention}" )
        embed.add_field(
            name = "hues",
            value = 'Array of hue numbers (`+pic hues`), with the same amount of elements as used for friendly_colors',
            inline = False
        )
        embed.add_field(
            name = "station_regeneration",
            value = 'Factor to apply to station shield regen',
            inline = False
        )
        embed.add_field(
            name = "station_size",
            value = 'Size of the station; integer from 1 to 5',
            inline = False
        )
        embed.add_field(
            name = "station_crystal_capacity",
            value = 'Factor to apply to the station crystal capcity, range [0.1,10]',
            inline = False
        )
        embed.add_field(
            name = "station_repair_treshold",
            value = 'Part of station crystal capcity that must be refilled to repair a module. In the range [0.1,10]',
            inline = False
        )
        embed.add_field(
            name = "auto_assign_teams",
            value = 'Allow assigning players to a specific team (true) or let them choose the team themselves (false).',
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "options team",ctx.guild.name)
    elif optionsType_ == "main" or optionsType_ == "common":
        embed = discord.Embed(color = 0xDA7B44, title ="Main this.options options", description = f"Asked by {ctx.message.author.mention}" )
        embed.add_field(
            name = "root_mode",
            value = 'The mod to inherit from: "survival", "team", "invasion", "deathmatch", "battleroyale" or " " (undefined mode)',
            inline = False
        )
        embed.add_field(
            name = "reset_tree",
            value = 'Set true to remove the original ship tree',
            inline = False
        )
        embed.add_field(
            name = "ships",
            value = 'An array of ships to add to the tree',
            inline = False
        )
        embed.add_field(
            name = "map_size",
            value = 'Size of the map, range from 20 to 200',
            inline = False
        )
        embed.add_field(
            name = "soundtrack",
            value = '"procedurality.mp3", "argon.mp3", "crystals.mp3", "red_mist.mp3", "civilisation.mp3" or "warp_drive.mp3" or none',
            inline = False
        )
        embed.add_field(
            name = "max_players",
            value = 'From 1 to 240',
            inline = False
        )
        embed.add_field(
            name = "lives",
            value = 'Number of lives, from 1 to 5',
            inline = False
        )
        embed.add_field(
            name = "max_level",
            value = 'Max level you can reach, from 1 to 7',
            inline = False
        )
        embed.add_field(
            name = "friendly_colors",
            value = 'Serves to define teams; how many teams (or 0, maximum 5)',
            inline = False
        )
        embed.add_field(
            name = "map_name",
            value = 'Name of the map',
            inline = False
        )
        embed.add_field(
            name = "survival_level",
            value = 'Level which triggers survival mode (8 for no trigger, 2 minimum)',
            inline = False
        )
        embed.add_field(
            name = "starting_ship",
            value = 'Enter desired ship code: 101,201,404, etc',
            inline = False
        )
        embed.add_field(
            name = "starting_ship_maxed",
            value = 'true or false',
            inline = False
        )
        embed.add_field(
            name = "frictio_ratio",
            value = '0 to 2',
            inline = False
        )
        embed.add_field(
            name = "strafe",
            value = 'Strafing speed factor, an integer from 0 to 1',
            inline = False
        )
        embed.add_field(
            name = "speed_mode",
            value = '0 to 2',
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        message = await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "options main",ctx.guild.name)
        def waitEmoji(reaction, user):
            return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji)== "➡️") 
        await message.add_reaction("➡️")
        reaction, user = await bot.wait_for("reaction_add", timeout=10, check = waitEmoji)
        if reaction.emoji == "➡️":
            embed = discord.Embed(color = 0xDA7B44, title ="Main this.options options", description = f"Asked by {ctx.message.author.mention}" )
            embed.add_field(
                name = "rcs_toogle",
                value = 'true or false',
                inline = False
            )
            embed.add_field(
                name = "map_id",
                value = 'Number in the range [0-999]',
                inline = False
            )
            embed.add_field(
                name = "map_density",
                value = 'Density of the map (0 to 2)',
                inline = False
            )
            embed.add_field(
                name = "weapon_drop",
                value = '0 to 10 (probability that an asteroid will drop a weapon)',
                inline = False
            )
            embed.add_field(
                name = "crystal_drop",
                value = 'Percentage of gems can be collected when a ship drain gems',
                inline = False
            )
            embed.add_field(
                name = "release_crystals",
                value = 'true/false for allowing/forbidding [V] to release gems',
                inline = False
            )
            embed.add_field(
                name = "mines_self_detroy",
                value = 'true or false',
                inline = False
            )
            embed.add_field(
                name = "mines_destroy_delay",
                value = 'All alnded mines will be destroyed after this interval if no enemies triggered the mines (in ticks) mminimum 0, no actual maximum limit (highest ever reached is 10^308)',
                inline = False
            )
            embed.add_field(
                name = "healing_enabled",
                value = 'true or false',
                inline = False
            )
            embed.add_field(
                name = "healing_ratio",
                value = '0 to 2',
                inline = False
            )
            embed.add_field(
                name = "shield_regen_factor",
                value = 'Minimum 0, no actual limit (highest ever reached is 10^308)',
                inline = False
            )
            embed.add_field(
                name = "invulnerable_ships",
                value = 'Ships are invulnerable or not (true/false)',
                inline = False
            )
            embed.add_field(
                name = "weapons_store",
                value = 'Set to false to remove access to the weapon store',
                inline = False
            )
            embed.add_field(
                name = "radar_zoom",
                value = 'Set value to 1,2 or 4',
                inline = False
            )
            embed.add_field(
                name = "auto_refill",
                value = 'When set to true, collecting an energy or shield pill immediately refills energy or shield ; the colelcted pill is not added to the active weapons',
                inline = False
            )
            embed.add_field(
                name = "projectile_speed",
                value = 'Affects the speed of rockets, missiles and torpedoes ; use 1 for default speed (minimum 0, no actual maximum limit (highest ever reached is 10^308))',
                inline = False
            )
            embed.add_field(
                name = "choose_ship",
                value = 'E.g. setting to [301,302,303] will let player choose a ship from these 3 ships before entering the game',
                inline = False
            )
            embed.add_field(
                name = "collider",
                value = 'Enable/disable (true/false) collisions of player ships with anything',
                inline = False
            )
            embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
            await message.edit(embed = embed )
    elif optionsType_ == "survival mode" or optionsType_ == "survival":
        embed = discord.Embed(color = 0xDA7B44, title ="Survival mode this.options options", description = f"Asked by {ctx.message.author.mention}" )
        embed.add_field(
            name = "survival_time",
            value = 'When to trigger survival mode ; 0 or valie in minutes',
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
    elif optionsType_ == 'deathmatch' or optionsType_ == "pdm":
        shipGroup = [
        '    ship_groups: [\n'
        +'        ["U-Sniper","Howler"],\n'
        +'        ["Crusader", "Pioneer"]\n'
        +'    ]\n'
        ]
        embed = discord.Embed(color = 0xDA7B44, title ="Deathmatch mode this.options options", description = f"Asked by {ctx.message.author.mention}" )
        embed.add_field(
            name = "ship_groups",
            value = 'An array containing some arrays, each of them representing one ship group (by name) available for selection, see example below. The longer the array is, the lower change for each ship group being available in a single match'
            + f"\n\n```js\n{shipGroup[0]}```",
            inline = False
        )
        embed.set_author(name="Wolfan modding station", url="https://discord.gg/vpSQd29SEM", icon_url="https://cdn.discordapp.com/attachments/797426986867228693/861138579111804928/wolfanmoddinglogo.png")
        await ctx.send(embed = embed)
        await sendChat(ctx.message.author.mention, "options deathmatch",ctx.guild.name)
    else:
        message =  await ctx.send(f"{ctx.message.author.mention} unknown field of options. Please choose a mode between `survival mode`, `deathmatch`, `team mode`, `main`.")
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "options",ctx.guild.name)

@bot.command()
async def soundtrack(ctx, soundtrack):
    soundtrackName = str.lower(soundtrack)
    if soundtrackName == "procedurality":
        await ctx.send(
            "https://open.spotify.com/track/0t6yCP4a4K3uLzsep7TgBk?si=a48b1af17aff49b9"
        )
        await sendChat(ctx.message.author.mention, "soundtrack: procedurality",ctx.guild.name)
    elif soundtrackName == "argon":
        await ctx.send(
            "https://open.spotify.com/track/5FPjb6MVHx3bPAx9ZGpt7c?si=67568c851fd74d38"
        )
        await sendChat(ctx.message.author.mention, "soundtrack: argon",ctx.guild.name)
    elif soundtrackName == "crystals":
        await ctx.send(
            "https://open.spotify.com/track/6vpQWLMjGocdRrbGbyc0is?si=fb7e2a1d68d14a10"
        )
        await sendChat(ctx.message.author.mention, "soundtrack: crystals",ctx.guild.name)
    else:
        message = await ctx.send(f"{ctx.message.author.mention} unknown soundtrack, please choose between `procedurality`, `argon` or `crystals`.")
        await asyncio.sleep(10)
        await message.delete()
        await sendChat(ctx.message.author.mention, "soundtrack",ctx.guild.name)


bot.run('')











