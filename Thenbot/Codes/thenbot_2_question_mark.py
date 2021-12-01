import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import random
import asyncio



bot = commands.Bot(command_prefix = "o,")
bot.remove_command("help")
bot.remove_command("credits")


#Things to do:
# - Nautic Series
# - Events: AOW, ACW, etc
# - CTF ships (??)

##python C:\Users\Utilisateur\Documents\Codage\Thenbot\e.py


@bot.event
async def on_ready():
    print("Bot ready !")


@bot.command()
async def test(ctx, *value):
    message_content = " ".join(value)
    Value = str.lower(message_content)

    level = ["1","2","2","3","3","3","3","4","4","4","4","4","4","5","5","5","5","5","5","5","6","6","6","6","6","6","6","6","7","7","7","7"]
    model = ["1","1","2","1","2","3","4","1","2","3","4","5","6","1","2","3","4","5","6","7","1","2","3","4","5","6","7","8","1","2","3","4"]
    mass = ["60","80","100","120","90","70","200","200","200","250","120","250","250",]
    shieldCap = ["75/100","100/120","125/175"]
    shieldRegen = ["2/3","3/4","3/5"]
    energyCap = ["40/60","50/80","50/80"]
    energyRegen = ["10/15","15/25","15/20"]
    cannonDamage = ["5/6","3/5","4/8"]
    cannonNumber = ["1","3","2"]
    turningRate = ["110/130","60/100","70/85","60/80","50/70","35/60","40/60","90/120","60/90","50/90","50/100","40/80","40/70","50/70","120/180","50/80","70/90","35/48","70/95","40/70","30/50","50/70","60/80","50/70","60/80","50/70","60/80","50/70","60/80","50/70","30/45","30/45","20/20","35/35","15/15","20/20"]
    Acceleration = ["100/120","100/120","90/110","80/100","100/130","130/150","70/80","60/80","60/80","90/100","100/140","50/100","80/100","60/110","150/180","90/120","110/130","140/190","90/120","90/100","70/100","80/100","80/120","80/120","90/140","80/90","130/150","60/90","150/150","90/90","125/125","150/150"]
    terminalVelocity = ["125/145","110/135","110/135","105/120","100/120","120/155","80/100","75/90","85/105","75/100","80/110","90/120","75/100","75/90","70/100","80/90","90/100","110,140","85/120","70/90","70/80","75/90","70/110","75/105","90/115","75/90","70/90","70/80","45/45","130/130","80/80","40/40"]
    maker = ["Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Kleinmen","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality","Neuronality"]

    ships = ["fly","delta fighter", "trident","pulse fighter", "side fighter", "shadow x1", "y defender", "vanguard","mercury","x warrior","side interceptor","pioneer","crusader","usniper","furystar","t warrior","aetos","shadow x2","howler","bat defender","advanced fighter","scorpion","maurauder","condor","a speedster","rock tower","barracuda","o defender","odyssey","shadow x3","bastion","aries"]
    capName = ["Fly","Delta-Fighter", "Trident","Pulse-Fighter", "Side-Fighter", "Shadow-X1", "Y-Defender", "Vanguard","Mercury","X-Warrior","Side Interceptor","Pioneer","Crusader","U-Sniper","Furystar","T-Warrior","Aetos","Shadow-X2","Howler","Bat-Defender","Advanced-Fighter","Scorpion","Maurauder","Condor","A-Speedster","Rock-Tower","Barracuda","O-Defender","Odyssey","Shadow-X3","Bastion","Aries"]

    thumbnail = [
        "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/0c/Fly.png/revision/latest/scale-to-width-down/241?cb=2020012105501",
        "https://starblastio.gamepedia.com/File:Delta1.png",
        "https://starblastio.gamepedia.com/File:Delta1.png",
    ]
    for ship in ships:
        if ship == Value:
            myValue = ships.index(ship)
            embed = discord.Embed(title= f"**{capName[int(myValue)]}**", description= f"Asked by {ctx.message.author.mention}\nShip made by Neuronality.") 
            embed.set_thumbnail(url=f"{thumbnail[int(myValue)]}")
            embed.add_field(name= "Infos", value = f"Level: {level[int(myValue)]}\nModel: {model[int(myValue)]}\nMass: {mass[int(myValue)]}", inline = False)
            embed.add_field(name= "Shield", value = f"Cap : {shieldCap[int(myValue)]}\nRegen : {shieldRegen[int(myValue)]}", inline= False )
            embed.add_field(name= "Energy", value = f"Cap : {energyCap[int(myValue)]}\nRegen : {energyRegen[int(myValue)]}\nCannon damage/shot : {cannonDamage[int(myValue)]} ({cannonNumber[int(myValue)]} lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = f"{turningRate[int(myValue)]}" , inline= False)
            embed.add_field(name= "Acceleration", value = f"{Acceleration[int(myValue)]}" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = f"{terminalVelocity[int(myValue)]}" , inline= False)
            await ctx.send(embed = embed)


@bot.command()
async def aliens(ctx, *alienName):
    AlienName = str.lower(" ".join(alienName))

    health = ["10","20","50","1000","30","60","120","1200","2500","80","80"]
    regenPerS = ["0","1","2","2","1","2","3","2","6","1","2"]
    damagePerShot = ["8","10","15","30","8","10","15","15","50","4","5"]
    firingRate = ["1","2","3","2","5","5","5","3","2","2","3"]
    blastSpeed = ["90","100","100","90","80","80","100","110","130","120","130"]
    mass = ["50","100","200","600","50","80","150","500","1000","70","60" ]
    waves = ["1,2,3,5","1,2,3","5","2","2,3","3,5,10","5,7,10","3","7","5,9","6"]
    pointDrop = ["10","20","50","1000","30","60","120","1200","2500","80","80"]

    aliens = []
    Maliens = []

    for alien in aliens:
        if alien == AlienName:
            myValue = int(aliens.index(alien))
            embed = discord.Embed(title= "**__Yellow Crab__**", description = "") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4e/FighterMKll.png/revision/latest/scale-to-width-down/200?cb=20171112213854")
            embed.add_field(name="Health", value= "60", inline = False)
            embed.add_field(name="Regen/sec.", value= "2", inline = False)
            embed.add_field(name="Damage/shot", value= "10", inline = False)
            embed.add_field(name="Firing Rate", value= "5", inline = False)
            embed.add_field(name="Blast Speed", value= "80", inline = False)
            embed.add_field(name="Mass", value= "80", inline = False)
            embed.add_field(name="Waves", value= "3,5,10", inline = False)
            embed.add_field(name= "Point Drop", value= "60", inline = False)
            await ctx.send(embed = embed)






@bot.command()
async def sbhelp(ctx):
    user = ctx.message.author.mention
    embed = discord.Embed(title= "**__Starblast commands: help__**", description= f"Asked by {ctx.message.author.mention}\nMake sure you type the commands without any capital letters.\n__Commands relating to the different starblast modes:__\n\n• `o,modes`,\n • `o,teammode`,\n• `o,survival`,\n• `o,invasion`,\n• `o,deathmatch`,\n• `o,alieninstrusion`,\n• `o,battleroyale`,\n• `o,ctf`,\n• `o,nauticseries`,\n• `o,racing`,\n• `o,rumble`,\n• `o,useries`. \n\n\n\nIf you are looking for a particular ship, you must type the corresponding mod according to the desired ship:\n• Alien Intrusion: `o,alienintrusionships`, \n• Battle Royale ships: `o,battleroyaleships`,\n• Capture the flag: `o,ctfships`,\n• Nautic Series: `o,nauticships`,\n• Racing mod: `o,racingships`,\n• U-Series: `useriesships`. \n\n\n\n**Enjoy using orgono bot !** :smiley:") 
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/765971859765854270/770933010500550677/Capture_decran_du_2020-10-27_18-28-18.png")
    message = "The help sheet was sent to you privately!"
    await ctx.send(embed = embed)

@bot.command()
async def infos(ctx):
    user = ctx.message.author.mention
    embed = discord.Embed(title = "**__ORGONO BOT__**", description = "\nI was designed for the purpose of quickly documenting on starblast.io. When you're looking for a specific thing, just type the search command: \n`o,TheThingYouWantToSearch`\n\n\nEvery element relating to starblast will be in this bot. It will allow you to receive information quickly and easily.\n\n\nIf you have any suggestions, feedback or ideas for me, please feel free to contact my creator Wolfan on discord (**WOLFΛИ # 5534**) and come to support for this bot: ** https: //discord.gg/ jT2d7Wu **.")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/765971859765854270/770933010500550677/Capture_decran_du_2020-10-27_18-28-18.png")
    await ctx.send(embed = embed)


@bot.command()
async def help(ctx):
    help = [

    ]
    embed = discord.Embed(title = "**__Help__**", description = "\nHello <:happypiranha:771873100098043954>! Let me help you! \n\nType `o,TheThingYouSearch` if you are looking for something on starblast. **Never use capitals when doing this type of command, otherwise it won't work.**\n\nType `o,infos` for more info about me.\n\nType `o,invite` to invite me in your server.\n\nType `o,logs` to see new things about me.\n\nType `o,admin`to see the differents reserved commands. ")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/765971859765854270/770933010500550677/Capture_decran_du_2020-10-27_18-28-18.png")
    await ctx.send(embed = embed)






@bot.command()
async def ecp(ctx):
    embed = discord.Embed(title= "**__ECP__ :**", description = f"\nECP means 'Elite commander pass' and cost a certain amount of money. You can do several things with it such as: \n- Code ships and mods, \n- Have a different ship and laser skin than normal (with multiple choices, \n- Have a badge visible in-game that you can choose, \n- Have access to items still in the testing phase, \n- Have a Tier 1 ship maxed out at the start of each game, \n- Be able to rank in deathmatch, \n- etc. \n \n \nYou can find more information about this [here](https://starblastio.gamepedia.com/Elite_Commander_Pass).")
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/3/32/Gamepedia_Badge.png/revision/latest/scale-to-width-down/246?cb=20190530195218")
    await ctx.send(embed = embed)



@bot.command()
async def modhelp(ctx):
    embed = discord.Embed(title = "**__Need help in modding ?__**", description ="\nHere are some usefull things:\n- [Vocabulary](https://starblast.io/glyphs.html) stuff,\n- [Modding Documentation](https://github.com/pmgl/starblast-modding),\n- Starblast modding modules: [ship editor](https://starblast.io/shipeditor/), [mod editor](https://starblast.io/modding.html),\n- Starblast [map editor](https://bhpsngum.github.io/starblast/mapeditor/).\n\n\nIf you need some modding tutorials, type `o,tutorial` to receive a help sheet in DM. ")
    
    await ctx.send(embed=embed)

@bot.command()
async def tutorial(ctx):
    embed = discord.Embed(title = "**__Starblast modding tutorials__**", description ="\nHere are some links.\nVideo tutorials:\n- [A T K](https://www.youtube.com/watch?v=r916KbgQ82w&t) (general),\n- [Interdictor](https://www.youtube.com/watch?v=waT0qT6nxo8) (background),\n- [Interdictor](https://www.youtube.com/watch?v=3b2zKArOkXk) (ship),\n- [Lexagon](https://www.youtube.com/watch?v=VkBjgtQpy1A) (general),\n- [Lexagon](https://www.youtube.com/watch?v=fy4tABmKkQU) (ship),\n- [Wolfan](https://www.youtube.com/watch?v=35SM5rFteIs&t) (general).\n\nWritten tutorials:\n- [Kleinem](https://starblastio.gamepedia.com/Ship_Editor_Tutorial) (ship),\n- [Malerfor](https://starblastio.gamepedia.com/Advanced_Ship_Editing) (advanced ship). \n\n\n\nGeneral mean **make a ship and test it**.\nShip editor mean [self explanatory].\nBackground mean **add a background to the game**  ")
    await ctx.send(embed=embed)




@bot.command()
async def modes(ctx, *gameMode):
    messagecontent = " ".join(gameMode)
    GameMode = str.lower(messagecontent)
    if GameMode == "alien intrusion":
        embed = discord.Embed(title="**__Starblast Alien Intrusion:__**", description = f"\nIn this mode, mining is unnecessary. The asteroids break very quickly and don't give any gems. \nYou must go to the center of the map and kill aliens to collect gems. The aliens appear in some sort of town. The gem capacity of the station is above average. \n \nAll mod was developed by Goldman, also the ship tree. \n \n \nMore information about this mod [here](https://starblastio.gamepedia.com/Alien_Intrusion).\nYou can also find the current version or Alien Intrusion [here](https://pastebin.com/uH4ywYnh ).")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/d8/AlienIntrusion5.0Banner.PNG/revision/latest/scale-to-width-down/449?cb=20190914234600")
        await ctx.send(embed = embed)
    elif GameMode == "battle royale":
        embed = discord.Embed(title="**__Starblast Battle  Royale:__**", description = f"\nStarblast battle royale is a mod developed by the developers. However, the ships were made by Kleinem, SchickenMan, Finalizer and Goldman. \nThe goal of this game mode is to kill everyone else, collecting secondaries at different points on the map. But be careful, your ship cannot regenerate its shield on its own. You must collect secondaries which will increase the life of your shield. To prevent some players from escaping, a gravitational field is in action throughout the game. \n\n\nMore information on this mod [here](https://starblastio.gamepedia.com/Battle_Royale).")
        
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/f4/Battleroyale.jpg/revision/latest/scale-to-width-down/360?cb=20190820091719")
        await ctx.send(embed = embed)
    elif GameMode == "capture the flag" or GameMode == "ctf":
        embed = discord.Embed(title="**__Starblast Capture The Flag (CTF):__**", description = f"\nCapture The Flag is a mod developed by 45rfew and Bhpsngum. The goal is simple: grab the skin of the opposing team and take them to their team's camp. \nThis mod uses the vanilla ship tree and the 45rfew mod, the money mod. \n \nThis mod is coded so that the game never stops. Indeed, when the time is up, the ships change, the timer is reset and the game starts again. \n \n` [There is no more information available on gamepedia for the moment]`.")
        
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/769081274421477447/769169002952916995/Vignette_CaptureTheFlag.png")
        await ctx.send(embed = embed)
    elif GameMode == "nautic series":
        embed = discord.Embed(title="**__Starblast Nautic Series:__**", description = f"\nNautic Series is a mod developed by Goldman. The ship tree is a ship tree made up of vessels that resemble marine animals. \nThe resort's gem capacity is well above average. However, gems have a high value. \n \n More info on this mod [here](https://starblastio.gamepedia.com/Nautic_Series).\nYou can also find the current version of Nautic Series [here](https://pastebin.com/ciyyc8qK ).")
        
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4d/Nauticseries.jpg/revision/latest/scale-to-width-down/300?cb=20190219051942")
        await ctx.send(embed = embed)
    elif GameMode == "racing":
        embed = discord.Embed(title="**__Starblast Nautic Series:__**", description = f"\nNautic Series is a mod developed by Goldman. The ship tree is a ship tree made up of vessels that resemble marine animals. \nThe resort's gem capacity is well above average. However, gems have a high value. \n \n More info on this mod [here](https://starblastio.gamepedia.com/Nautic_Series).\nYou can also find the current version of Nautic Series [here](https://pastebin.com/ciyyc8qK ).")
        
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4d/Nauticseries.jpg/revision/latest/scale-to-width-down/300?cb=20190219051942")
        await ctx.send(embed = embed)
    elif GameMode == "rumble":
        embed = discord.Embed(title="**__Starblast Rumble mod:__**", description = f"\nThe rumble mod, developed by 45rfew, is a deathmatch, but in a team. Two teams compete to try to win the most points within a time limit. You can have a game that lasts 30 minutes where you have to get 100 points and another of 15 minutes or you have to get 50. \n At the end of the allotted time, if no team has managed to get the required points, the team with the most wins. \nThis mod uses the vannilla ship tree. \n \nMore info about this mod [here](https://starblastio.gamepedia.com/Rumble).")
        
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/a/ad/RumblePoster1.0.png/revision/latest/scale-to-width-down/300?cb=20200904231053")
        await ctx.send(embed = embed)
    elif GameMode == "u series" or GameMode == "u-series":
        embed = discord.Embed(title="**__Starblast U-Series:__**", description = f"\nThis mod was developed by Finalizer. It is a mod that has a ship tree developed around the U-Sniper ship. \nThe station's capacity is normal, although the ships are very powerful. Vessels mine easily, attack easily, and for some can escape easily. \nMany backgrounds can be found in this mod, also developed by Finalizer. \n \nMore information about this mod [here](https://starblastio.gamepedia.com/U-Series). You can also find the current version of U-Series [here](https://pastebin.com/fWBx86GW ).")
        
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/5f/Useries.jpg/revision/latest/scale-to-width-down/360?cb=20181011032805")
        await ctx.send(embed = embed)
    elif GameMode == "dtm" or GameMode == "destroy the mothership":
        await ctx.send('to do')
    elif GameMode == "sdc":
        await ctx.send('to do')




@bot.command()
async def maps(ctx, type):
    message_content = " ".join(type)
    Type = str.lower(message_content)
    if Type == "main" :
        embed = discord.Embed(title = "**__Starblast modes Maps__**", description = "There are different maps made by players, and in two different modes: Rumble and Starblast racing Championship. To see the different maps for each mode, type `o, [mode]maps` (`o,racinmaps` for SRC).")
        await ctx.send(embed =embed)
    elif Type == "racing":
        embed = discord.Embed(title = "**__SRC maps__**", description = "Here are the differents starblast SRC's maps:\n- Chinese GP (type `o,chinesegp`),\n- Azerbaijani GP (type `o,azerbaijanigp`),\n- Austrian GP (type `o,austriangp`),\n- British GP (type `o,britishgp`),\n- Hungarian GP (type `ohungariangp`),\n- Belgian GP (type `o,belgiangp`),\n- Italian GP (type `italiangp`),\n- Russian GP (type `o,russiangp`),\n- Japanese Gp (`o,japanesegp`),\n- USA Sprint GP (type `o,usasprintgp`),\n- USA Endurance GP (type `o,usaendurencegp`).")
        await ctx.send(embed =embed)@bot.command()
    elif Type == "rumble":
        embed = discord.Embed(title = "**__Rumble mod maps__**", description = "Here are the differents starblast rumble's maps:\n- Dimension by Healer,\n- Waves by Kirito,\n- Atoms by 45rfew,\n- Boxes 2.0 by Eden,\n- Slides by Healer,\n- Rammers's paradise by Destroy,\n- Barriers by Healer.\n\nIf you want to see how does these maps looks like, just type `o,[mapname]`.\n\nNote:\nType `o,boxes` for Boxes 2.0 map and `o,rammersparadise` for Rammer's Paradise map.")
        user = ctx.message.author.mention
        await ctx.send(embed =embed)
    elif Type == "ctf" or Type == "capture the flag":
        await ctx.send("to do")


@bot.command()
async def map(ctx, mode, *name):
    GameMode = str.lower(mode)
    message_content = " ".join(name)
    mapName = str.lower(message_content)
    if GameMode == "racing":
        if mapName == "chinese gp":
            embed = discord.Embed(title = "**Map: Chinese GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/78/ChineseGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706150957")
            await ctx.send(embed = embed)
        elif mapName == "azerbaijani gp":
            embed = discord.Embed(title = "**Map: Azerbaijani GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/6c/AzerbajaniGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706151322")
            await ctx.send(embed = embed)
        elif mapName =="austrian gp":
            embed = discord.Embed(title = "**Map: Austrian GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/02/AustrianGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706151556")
            await ctx.send(embed = embed)
        elif mapName == "british gp":
            embed = discord.Embed(title = "**Map: British GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/b/b7/BritishGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706151732")
            await ctx.send(embed = embed)
        elif mapName == "hungarian gp":
            embed = discord.Embed(title = "**Map: Hungarian GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/2/28/HungarianGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706151931")
            await ctx.send(embed = embed)
        elif mapName == "belgian gp":
            embed = discord.Embed(title = "**Map: Belgian GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/73/BelgianGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706152153")
            await ctx.send(embed = embed)
        elif mapName == "italian gp":
            embed = discord.Embed(title = "**Map: Italian GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/73/BelgianGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706152153")
            await ctx.send(embed = embed)
        elif mapName == "russian gp":
            embed = discord.Embed(title = "**Map: Russian GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/c/c5/RussianGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706152604")
            await ctx.send(embed = embed)
        elif mapName == "japanese gp":
            embed = discord.Embed(title = "**Map: Japanese GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/8f/JapaneseGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706152820")
            await ctx.send(embed = embed)
        elif mapName == "usaprint gp":
            embed = discord.Embed(title = "**Map: USA Sprint GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/76/USASprintGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706153026")
            await ctx.send(embed = embed)
        elif mapName == "usaendurance gp":
            embed = discord.Embed(title = "**Map: USA Endurance GP**", description = "")
            embed.set_image(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/78/USAEnduranceGP_Map.PNG/revision/latest/scale-to-width-down/200?cb=20200706153332")
            await ctx.send(embed = embed)














@bot.command()
async def dimension(ctx):
    embed = discord.Embed(title = "**Map: Dimension**", description = "Map made by Healer")
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/04/DimensionMap.png/revision/latest/scale-to-width-down/400?cb=20200909081844")
    await ctx.send(embed = embed)


@bot.command()
async def waves(ctx):
    embed = discord.Embed(title = "**Map: Waves**", description = "Map made by Kirito")
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/0c/WavesMap.png/revision/latest/scale-to-width-down/400?cb=20200909082501")
    await ctx.send(embed = embed)


@bot.command()
async def atoms(ctx):
    embed = discord.Embed(title = "**Map: Atoms**", description = "Map made by 45rfew")
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/db/AtomsMap.png/revision/latest/scale-to-width-down/400?cb=20200909083702")
    await ctx.send(embed = embed)


@bot.command()
async def boxes(ctx):
    embed = discord.Embed(title = "**Map: Boxes**", description = "Map made by Eden")
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/07/Boxes2.0Map.png/revision/latest/scale-to-width-down/400?cb=20200909084139")
    await ctx.send(embed = embed)


@bot.command()
async def slides(ctx):
    embed = discord.Embed(title = "**Map: Slides**", description = "Map made by Healer")
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/0e/SlidesMap.png/revision/latest/scale-to-width-down/400?cb=20200909085404")
    await ctx.send(embed = embed)


@bot.command()
async def rammersparadise(ctx):
    embed = discord.Embed(title = "**Map: Rammer's paradise**", description = "Map made by Destroy")
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/50/RammersParadiseMap.png/revision/latest/scale-to-width-down/400?cb=20200909085845")
    await ctx.send(embed = embed)


@bot.command()
async def barriers(ctx):
    embed = discord.Embed(title = "**Map: Barriers**", description = "Map made by Healer")
    embed.set_thumbnail(url = "https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/fd/BarriersMap.png/revision/latest/scale-to-width-down/400?cb=20200909090135")
    await ctx.send(embed = embed)


















@bot.command()
async def starblast(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**__Starblast__**:", description= f"asked by {ctx.message.author.mention}\n**[Starblast](https://starblast.io/) was created by Mathias and Gilles.\nHere is differents links that can be usefull for you if you want to learn more about starblast** :smiley:\n- [Neuronality](https://neuronality.com) website,\n- Starblast on [steam](https://store.steampowered.com/app/673260/Starblast/),\n- Starblast on [ich.io](https://neuronality.itch.io/starblast), \n- Official [wiki](https://starblastio.gamepedia.com), \n- Official [subbreddit](https://www.reddit.com/r/Starblastio/), \n\n**Contact:**\n- Neuronality's e-mail: *contact@neuronality.com*, \n- Neuronality's website [support](https://neuronality.com/#contact).")
    embed.set_thumbnail(url="https://starblast.io/static/img/starblast.png?1")
    await ctx.send(embed=embed)



@bot.command()
async def battleroyaleships(ctx):
    embed = discord.Embed(title="**Battle Royale ships:**", description ="\nRenegade, Cronus, Intrepid, Stingray, Hammer\n\nRemoved ships: Spearhead, Silencer, Cayman\n\n\nIf you want more information about a ship, type `o,TheShipYouWant`. ")
    embed.set_thumbnail(url="https://starblastio.gamepedia.com/File:Battleroyale.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def ctfships(ctx):
    embed = discord.Embed(title="**Capture the flag ships:**", description ="\n:warning: Not enough information found for this research :warning:")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/292251288903614464/763675137358299146/Vignette_CaptureTheFlag.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def nauticseriesships(ctx):
    embed = discord.Embed(title="**Nautic Series ships:**",description ="\nTier 1: Snail\nTier 2: Jellyfish, Crab\nTier 3: Squid, Archerfish, Guitarfish, Turtle\nTier 4: Cuttlfish, Lionfish, Lobster, Scad Fish, Stingray, Flying fish, Starfish\nTier 5: Swordfish, Giant Squid, Catfish, Dolphin, Reef Shark, Prianha, Swafish, Leatherback Turtle, Spider Crab,\nTier 6: Narwhal, Orca, Octopus, Beaked Whale, Shark, Grouper Fish, Angler, Hammerhead Shark, Manta, Beluga\nTier 7: Colossal Squid, Fin Whale, Whale Shark, Cachalot\n\nRemoved ships: Mullet\n\n\nIf you want more information about a ship, type `o,TheShipYouWant`. ")
    embed.set_thumbnail(url="https://starblastio.gamepedia.com/File:Nauticseries.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def racingships(ctx):
    embed = discord.Embed(title="**Racing Chanmpionship ships:**",description ="\nBooster, Astarl Accelerator, V1, RAD Diamond Lancer, Vengar, Space Phantom, Zarion")
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/52/MS_poster.png/revision/latest/scale-to-width-down/300?cb=20200511073248")
    await ctx.send(embed = embed)



##Vanilla Stuff
@bot.command()
async def vanillaships(ctx):
    embed = discord.Embed(title="**Vanilla ships:**", description ="\nTier 1: Fly\nTier 2: Trident, Delta-Fighter\nTier 3: Side-Fighter, Pulse-Fighter, Shadow X-3, Y-Defender\nTier 4: Vanguard, Mercury, X-Warrior, Side-Interceptor, Pioneer, Crusader\nTier 5: U-Sniper, FuryStar, T-Warrior, Aetos, Shadow X-2, Howler, Bat-Defender\nTier 6: Advanced-Fighter, Scorpion, Marauder, Condor, A-Speedster, Rock-Tower, Barracuda, O-Defender\nTier 7: Odyssay, Shadow X-3, Bastion, Aries\n\nRemoved ships: H-Mercury, Toscain\n\n\nIf you want more information about a ship, type `o,TheShipYouWant`. ")
    embed.set_thumbnail(url="https://starblast.io/static/img/starblast.png?1")
    await ctx.send(embed = embed)

@bot.command()
async def teammode(ctx):
    embed = discord.Embed(title="**__Starblast team mode:__**", description =f"\nThis mode uses the vanilla ship tree (the basic ships). Mine, give gems to your base to improve it and unlock the different levels to destroy enemy teams!\n\nLearn more [here](https://starblastio.gamepedia.com/Team_Mode).\nYou can also find a basic team mode tutorial [here](https://starblastio.gamepedia.com/Team_mode_Tutorial).")
    
    embed.set_thumbnail(url="https://starblast.io/static/img/starblast.png?1")
    await ctx.send(embed = embed)

@bot.command()
async def invasion(ctx):
    embed = discord.Embed(title="**__Starblast invasion mode:__**", description =f"\nFight aliens in different increasingly harsh waves! Kill the bosses and try to win with your teammates, but be careful not to get killed, or you will lose the game! \nThis mod uses the vanilla ship tree. \n \nMore information on this mode [here](https://starblastio.gamepedia.com/Invasion). \nYou can also find a basic invasion mode tutorial [here](https://starblastio.gamepedia.com/Invasion_Tutorial).")
    
    embed.set_thumbnail(url="https://starblast.io/static/img/starblast.png?1")
    await ctx.send(embed = embed)

@bot.command()
async def survival(ctx):
    embed = discord.Embed(title="**__Starblast survival mode:__**", description = f"\nMine to reach the most powerful tier in the game and kill everyone, trying not to get yourself killed! \nThis mode uses the vanilla ship tree. \n\nMore information on this mode [here](https://starblastio.gamepedia.com/Survival_Mode).")
    
    embed.set_thumbnail(url="https://starblast.io/static/img/starblast.png?1")
    await ctx.send(embed = embed)

@bot.command()
async def deathmatch(ctx):
    embed = discord.Embed(title="**__Starblast deathmatch:__**", description = f"\nFight in a death match against other players and try to win the game by earning 12 points! You can be classified if you have an ECP. \nThe different ships and third parties used vary at random. This mode use the vanilla ship tree. \nDon't try mine, you won't be able to harvest anything! \n \nMore info on this game mode [here](https://starblastio.gamepedia.com/Pro_Deathmatch).")
    
    embed.set_thumbnail(url="https://starblast.io/static/img/starblast.png?1")
    await ctx.send(embed = embed)

@bot.command()
async def aliens(ctx):
    embed = discord.Embed(title= "**__Starblast Aliens__**", description = "\nThere are different types of aliens and different classes of aliens in these types of aliens.\nYou can find these aliens in Alien Intrusion and invasion mode.\n\nHere are the differents aliens classes (ranked from least strong to strongest):\n- Chicken: green, yellow, red, purple,\n- Crab: green, yellow, red,\n- Fortress: yellow, red,\n- Candlestick: green, yellow, red,\n- Hirsute: yellow, red,\nPiranha: green, yellow, red, purple,\n- Pointu: green, yellow, purple,\nFork: green, yellow, red\n- Saucer: yellow, red, purple,\n- FinalBoss: red, purple.\n\n\nIf you want more informations, you can click [here](https://starblastio.gamepedia.com/Alien) or to go faster, you can type `o,[alien][color]` (do not capitalize and paste the two words between them).")
    await ctx.send(embed = embed)


@bot.command()
async def greenchicken(ctx):
    embed = discord.Embed(title= "**__Green Chicken__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/78/Chicken_Green.PNG/revision/latest/scale-to-width-down/200?cb=20181225181013")
    embed.add_field(name="Health", value= "10", inline = False)
    embed.add_field(name="Regen/sec.", value= "0", inline = False)
    embed.add_field(name="Damage/shot", value= "8", inline = False)
    embed.add_field(name="Firing Rate", value= "1", inline = False)
    embed.add_field(name="Blast Speed", value= "90", inline = False)
    embed.add_field(name="Mass", value= "50", inline = False)
    embed.add_field(name="Waves", value= "1,2,3,5", inline = False)
    embed.add_field(name= "Point Drop", value= "10", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def yellowchicken(ctx):
    embed = discord.Embed(title= "**__Yellow Chicken__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/62/Chicken_Yellow.PNG/revision/latest/scale-to-width-down/200?cb=20181225181036")
    embed.add_field(name="Health", value= "20", inline = False)
    embed.add_field(name="Regen/sec.", value= "1", inline = False)
    embed.add_field(name="Damage/shot", value= "10", inline = False)
    embed.add_field(name="Firing Rate", value= "2", inline = False)
    embed.add_field(name="Blast Speed", value= "100", inline = False)
    embed.add_field(name="Mass", value= "100", inline = False)
    embed.add_field(name="Waves", value= "1,2,3", inline = False)
    embed.add_field(name= "Point Drop", value= "20", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def redchicken(ctx):
    embed = discord.Embed(title= "**__Red Chicken__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/d6/DroneMKlll.png/revision/latest/scale-to-width-down/200?cb=20171112213218")
    embed.add_field(name="Health", value= "50", inline = False)
    embed.add_field(name="Regen/sec.", value= "2", inline = False)
    embed.add_field(name="Damage/shot", value= "15", inline = False)
    embed.add_field(name="Firing Rate", value= "3", inline = False)
    embed.add_field(name="Blast Speed", value= "100", inline = False)
    embed.add_field(name="Mass", value= "200", inline = False)
    embed.add_field(name="Waves", value= "5", inline = False)
    embed.add_field(name= "Point Drop", value= "50", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def purplechicken(ctx):
    embed = discord.Embed(title= "**__Purple Chicken__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/3/31/DroneMKVl.png/revision/latest/scale-to-width-down/200?cb=20171112213444")
    embed.add_field(name="Health", value= "1000", inline = False)
    embed.add_field(name="Regen/sec.", value= "2", inline = False)
    embed.add_field(name="Damage/shot", value= "30", inline = False)
    embed.add_field(name="Firing Rate", value= "2", inline = False)
    embed.add_field(name="Blast Speed", value= "90", inline = False)
    embed.add_field(name="Mass", value= "600", inline = False)
    embed.add_field(name="Waves", value= "2", inline = False)
    embed.add_field(name= "Point Drop", value= "1000", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def greencrab(ctx):
    embed = discord.Embed(title= "**__Green Crab__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/1b/FighterMKl.png/revision/latest/scale-to-width-down/200?cb=20171112213701")
    embed.add_field(name="Health", value= "30", inline = False)
    embed.add_field(name="Regen/sec.", value= "1", inline = False)
    embed.add_field(name="Damage/shot", value= "8", inline = False)
    embed.add_field(name="Firing Rate", value= "5", inline = False)
    embed.add_field(name="Blast Speed", value= "80", inline = False)
    embed.add_field(name="Mass", value= "50", inline = False)
    embed.add_field(name="Waves", value= "2,3", inline = False)
    embed.add_field(name= "Point Drop", value= "30", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def yellowcrab(ctx):
    embed = discord.Embed(title= "**__Yellow Crab__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4e/FighterMKll.png/revision/latest/scale-to-width-down/200?cb=20171112213854")
    embed.add_field(name="Health", value= "60", inline = False)
    embed.add_field(name="Regen/sec.", value= "2", inline = False)
    embed.add_field(name="Damage/shot", value= "10", inline = False)
    embed.add_field(name="Firing Rate", value= "5", inline = False)
    embed.add_field(name="Blast Speed", value= "80", inline = False)
    embed.add_field(name="Mass", value= "80", inline = False)
    embed.add_field(name="Waves", value= "3,5,10", inline = False)
    embed.add_field(name= "Point Drop", value= "60", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def redcrab(ctx):
    embed = discord.Embed(title= "**__Red Crab__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/90/FighterMKlll.png/revision/latest/scale-to-width-down/200?cb=20171112214122")
    embed.add_field(name="Health", value= "120", inline = False)
    embed.add_field(name="Regen/sec.", value= "3", inline = False)
    embed.add_field(name="Damage/shot", value= "15", inline = False)
    embed.add_field(name="Firing Rate", value= "5", inline = False)
    embed.add_field(name="Blast Speed", value= "100", inline = False)
    embed.add_field(name="Mass", value= "150", inline = False)
    embed.add_field(name="Waves", value= "5,7,10", inline = False)
    embed.add_field(name= "Point Drop", value= "120", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def yellowfortress(ctx):
    embed = discord.Embed(title= "**__Yellow Fortress__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/5a/Fortress_yellow.png/revision/latest/scale-to-width-down/200?cb=20181225150528")
    embed.add_field(name="Health", value= "1200", inline = False)
    embed.add_field(name="Regen/sec.", value= "2", inline = False)
    embed.add_field(name="Damage/shot", value= "15", inline = False)
    embed.add_field(name="Firing Rate", value= "3", inline = False)
    embed.add_field(name="Blast Speed", value= "110", inline = False)
    embed.add_field(name="Mass", value= "500", inline = False)
    embed.add_field(name="Waves", value= "3", inline = False)
    embed.add_field(name= "Point Drop", value= "1200", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def redfortress(ctx):
    embed = discord.Embed(title= "**__Red Fortress__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/fb/Fortress_red.png/revision/latest/scale-to-width-down/200?cb=20181225150515")
    embed.add_field(name="Health", value= "2500", inline = False)
    embed.add_field(name="Regen/sec.", value= "6", inline = False)
    embed.add_field(name="Damage/shot", value= "50", inline = False)
    embed.add_field(name="Firing Rate", value= "2", inline = False)
    embed.add_field(name="Blast Speed", value= "130", inline = False)
    embed.add_field(name="Mass", value= "1000", inline = False)
    embed.add_field(name="Waves", value= "7", inline = False)
    embed.add_field(name= "Point Drop", value= "2500", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def greencandlestick(ctx):
    embed = discord.Embed(title= "**__Green Candlestick__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/5b/Candlestick_green.png/revision/latest/scale-to-width-down/200?cb=20181223144057")
    embed.add_field(name="Health", value= "80", inline = False)
    embed.add_field(name="Regen/sec.", value= "1", inline = False)
    embed.add_field(name="Damage/shot", value= "4", inline = False)
    embed.add_field(name="Lasers Number", description = "5", inline = False)
    embed.add_field(name="Firing Rate", value= "2", inline = False)
    embed.add_field(name="Blast Speed", value= "120", inline = False)
    embed.add_field(name="Mass", value= "70", inline = False)
    embed.add_field(name="Waves", value= "5,9", inline = False)
    embed.add_field(name= "Point Drop", value= "80", inline = False)
    await ctx.send(embed = embed)


@bot.command()
async def yellowcandlestick(ctx):
    embed = discord.Embed(title= "**__Yellow Candlestick__**", description = "") 
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/9c/Candlestick_yellow.PNG/revision/latest/scale-to-width-down/200?cb=20181223144143")
    embed.add_field(name="Health", value= "80", inline = False)
    embed.add_field(name="Regen/sec.", value= "2", inline = False)
    embed.add_field(name="Damage/shot", value= "5", inline = False)
    embed.add_field(name="Lasers Number", description = "5", inline = False)
    embed.add_field(name="Firing Rate", value= "3", inline = False)
    embed.add_field(name="Blast Speed", value= "130", inline = False)
    embed.add_field(name="Mass", value= "60", inline = False)
    embed.add_field(name="Waves", value= "6", inline = False)
    embed.add_field(name= "Point Drop", value= "80", inline = False)
    await ctx.send(embed = embed)







# Tier 1
@bot.command()
async def snail(ctx):
    embed = discord.Embed(title="**Snail**", description="\nShip made by Goldman.")
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/d2/Snail.png/revision/latest?cb=20190625023656"
    )
    embed.add_field(
        name="Infos", value="Level: 1\nModel: 1\nMass: 65", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  75/100\nRegen: 2/3", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  35/55\nRegen :  20/25\nCannon damage/shot :  4/6 (1 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="110/125", inline=False)
    embed.add_field(name="Acceleration", value="95/110", inline=False)
    embed.add_field(name="Terminal Velocity", value="130/140", inline=False)
    
    await ctx.send(embed=embed)


# Tier 2
@bot.command()
async def jellyfish(ctx):
    embed = discord.Embed(
        title="**Jellyfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/2/22/Jellyfish.png/revision/latest?cb=20190901174355"
    )
    embed.add_field(
        name="Infos", value="Level: 2\nModel: 1\nMass: 200", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  200/225\nRegen: 7/10", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  100/125\nRegen :  45/55\nThis ship uses a dash = 50/75",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="65/90", inline=False)
    embed.add_field(name="Acceleration", value="95/110", inline=False)
    embed.add_field(name="Terminal Velocity", value="95/110", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def crab(ctx):
    embed = discord.Embed(

        title="**Jellyfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/63/Crab.png/revision/latest?cb=20190427130001"
    )
    embed.add_field(
        name="Infos", value="Level: 2\nModel: 2\nMass: 200", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  150/200\nRegen: 4/6", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  100/130\nRegen :  30/45\nCannon damage/shot :  9/14 (2 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="100/125", inline=False)
    embed.add_field(name="Acceleration", value="95/110", inline=False)
    embed.add_field(name="Terminal Velocity", value="115/135", inline=False)
    
    await ctx.send(embed=embed)


# Tier 3
@bot.command()
async def squid(ctx):
    embed = discord.Embed(
    title="**Squid**", description="\nShip made by Goldman.")
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/81/Squid.png/revision/latest?cb=20190901174514"
    )
    embed.add_field(
        name="Infos", value="Level: 3\nModel: 1\nMass: 330", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  200/275\nRegen: 6/8", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  125/175\nRegen :  45/55\nCannon damage/shot :  15/20	 (1 laser)\nThis ship uses a dash = 15/25",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="100/125", inline=False)
    embed.add_field(name="Acceleration", value="95/110", inline=False)
    embed.add_field(name="Terminal Velocity", value="115/135", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def archerfish(ctx):
    embed = discord.Embed(

        title="**Archerfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/c/cc/Archerfish.png/revision/latest/scale-to-width-down/200?cb=20190903135948"
    )
    embed.add_field(
        name="Infos", value="Level: 3\nModel: 2\nMass: 135", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  150/200\nRegen: 5/7", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  150/200\nRegen :  35/55\nCannon damage/shot :  5/7(1 laser)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="110/130", inline=False)
    embed.add_field(name="Acceleration", value="75/90", inline=False)
    embed.add_field(name="Terminal Velocity", value="110/125", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def guitarfish(ctx):
    embed = discord.Embed(

        title="**Guitarfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/7e/Guitarfish.png/revision/latest/scale-to-width-down/200?cb=20190903133217"
    )
    embed.add_field(
        name="Infos", value="Level: 3\nModel: 3\nMass: 190", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  175/225\nRegen: 6/8", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  100/150\nRegen :  30/40\nCannon damage/shot :  17/22(2 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="70/90", inline=False)
    embed.add_field(name="Acceleration", value="70/90", inline=False)
    embed.add_field(name="Terminal Velocity", value="95/110", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def turtle(ctx):
    embed = discord.Embed(
title="**Turtle**", description="\nShip made by Goldman.")
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/e/e9/Turtle.png/revision/latest/scale-to-width-down/200?cb=20190903141002"
    )
    embed.add_field(
        name="Infos", value="Level: 3\nModel: 4\nMass: 165", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  150/200\nRegen: 5/7", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  125/175\nRegen :  45/60\nCannon damage/shot :  30/35 (1 laser)\n This ship uses a dash = 6/9",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="70/90", inline=False)
    embed.add_field(name="Acceleration", value="70/90", inline=False)
    embed.add_field(name="Terminal Velocity", value="95/110", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def cuttlefish(ctx):
    embed = discord.Embed(

        title="**Cuttlefish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/65/Cuttlefish.png/revision/latest/scale-to-width-down/200?cb=20190901174701"
    )
    embed.add_field(
        name="Infos", value="Level: 4\nModel: 1\nMass: 450", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  350/450\nRegen: 8/10", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  0.1/0.1\nRegen :  1/1\nThis ship uses a dash = 1/1",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="85/120", inline=False)
    embed.add_field(name="Acceleration", value="100/120", inline=False)
    embed.add_field(name="Terminal Velocity", value="165/175", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def lionfish(ctx):
    embed = discord.Embed(

        title="**Lionfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/b/bb/Lionfish.png/revision/latest/scale-to-width-down/200?cb=20190903134118"
    )
    embed.add_field(
        name="Infos", value="Level: 4\nModel: 2\nMass: 165", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  175/225\nRegen: 5/7", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  150/200\nRegen :  40/65\nCannon damage/shot :  5/7 (2 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="80/95", inline=False)
    embed.add_field(name="Acceleration", value="80/100", inline=False)
    embed.add_field(name="Terminal Velocity", value="110/120", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def lobster(ctx):
    embed = discord.Embed(

        title="**Lobster**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/9f/Lobster.png/revision/latest/scale-to-width-down/200?cb=20190903140127"
    )
    embed.add_field(
        name="Infos", value="Level: 4\nModel: 3\nMass: 175", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  175/225\nRegen: 5/7", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  175/225\nRegen :  55/70\nCannon damage/shot :  23/41 (3 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="80/100", inline=False)
    embed.add_field(name="Acceleration", value="65/80", inline=False)
    embed.add_field(name="Terminal Velocity", value="95/110", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def scadfish(ctx):
    embed = discord.Embed(

        title="**Scad Fish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/e/ed/ScadFish.png/revision/latest/scale-to-width-down/200?cb=20200120043419"
    )
    embed.add_field(
        name="Infos", value="Level: 4\nModel: 4\nMass: 160", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  150/200\nRegen: 4/6", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  95/125\nRegen :  27/37\nCannon damage/shot :  17/21 (1 laser)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="110/130", inline=False)
    embed.add_field(name="Acceleration", value="70/90", inline=False)
    embed.add_field(name="Terminal Velocity", value="135/145", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def nauticstingray(ctx):
    embed = discord.Embed(

        title="**Stingray **", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/9a/Stingray_%28Nautic_Series%29.png/revision/latest/scale-to-width-down/200?cb=20190903133344"
    )
    embed.add_field(
        name="Infos", value="Level: 4\nModel: 5\nMass: 230", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  200/250\nRegen: 6/8", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  150/200\nRegen :  40/55\nCannon damage/shot :  13/17	 (4 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="65/80", inline=False)
    embed.add_field(name="Acceleration", value="70/90", inline=False)
    embed.add_field(name="Terminal Velocity", value="90/105", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def flyingfish(ctx):
    embed = discord.Embed(

        title="**Flying Fish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/b/bc/Flying_Fish.png/revision/latest/scale-to-width-down/200?cb=20190903141121"
    )
    embed.add_field(
        name="Infos", value="Level: 4\nModel: 6\nMass: 165", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  175/225\nRegen: 4/6", inline=False)
    embed.add_field(
        name="Energy",
        value="Cap :  275/325\nRegen :  100/125\nCannon damage/shot :  35/60 (4 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="85/105", inline=False)
    embed.add_field(name="Acceleration", value="110/130", inline=False)
    embed.add_field(name="Terminal Velocity", value="90/110", inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def starfish(ctx):
    embed = discord.Embed(

        title="**Starfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/52/Starfish.png/revision/latest/scale-to-width-down/200?cb=20190625023608"
    )
    embed.add_field(
        name="Infos", value="Level: 4\nModel: 7\nMass: 220", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  200/250\nRegen: 6/8", inline=False)
    embed.add_field(
        name="Energy",
        value=f"Cap :  250/300\nRegen :  365/425\nCannon damage/shot :  {27 * 5}/{35*5} (5 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="95/110", inline=False)
    embed.add_field(name="Acceleration", value="100/115", inline=False)
    embed.add_field(name="Terminal Velocity", value="100/115", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def swordfish(ctx):
    embed = discord.Embed(

        title="**Swordfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/f7/Swordfish.png/revision/latest/scale-to-width-down/200?cb=20190901174835"
    )
    embed.add_field(
        name="Infos", value="Level: 5\nModel: 1\nMass: 350", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  275/350\nRegen: 11/13", inline=False)
    embed.add_field(
        name="Energy",
        value=f"Cap :  175/225\nRegen :  45/65\nThis ship use a dash = 75/100",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="90/115", inline=False)
    embed.add_field(name="Acceleration", value="100/115", inline=False)
    embed.add_field(name="Terminal Velocity", value="90/105", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def giantsquid(ctx):
    embed = discord.Embed(

        title="**Giant Squid**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/72/Giant_Squid.png/revision/latest/scale-to-width-down/200?cb=20190903134344"
    )
    embed.add_field(
        name="Infos", value="Level: 5\nModel: 2\nMass: 295", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  225/300\nRegen: 7/9", inline=False)
    embed.add_field(
        name="Energy",
        value=f"Cap :  225/300\nRegen :  100/150\nCannon damage/shot :  94.5/127 (3 lasers) + dash = 80/80",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="85/100", inline=False)
    embed.add_field(name="Acceleration", value="50/70", inline=False)
    embed.add_field(name="Terminal Velocity", value="160/170", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def catfish(ctx):
    embed = discord.Embed(

        title="**Catfish**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/99/Catfish.png/revision/latest/scale-to-width-down/200?cb=20190903135326"
    )
    embed.add_field(
        name="Infos", value="Level: 5\nModel: 3\nMass: 175", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  200/275\nRegen: 6/8", inline=False)
    embed.add_field(
        name="Energy",
        value=f"Cap :  225/275\nRegen :  120/145\nCannon damage/shot :  {12*11}/{18*11} (22 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="80/100", inline=False)
    embed.add_field(name="Acceleration", value="75/100", inline=False)
    embed.add_field(name="Terminal Velocity", value="100/115", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def dolphin(ctx):
    embed = discord.Embed(

        title="**Dolphin**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/0b/Dolphin.png/revision/latest/scale-to-width-down/200?cb=20190903140304"
    )
    embed.add_field(
        name="Infos", value="Level: 5\nModel: 4\nMass: 230", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  250/325\nRegen: 6/8", inline=False)
    embed.add_field(
        name="Energy",
        value=f"Cap :  225/275\nRegen :  75/100\nCannon damage/shot :  140/185 (3 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="80/100", inline=False)
    embed.add_field(name="Acceleration", value="80/95", inline=False)
    embed.add_field(name="Terminal Velocity", value="80/90", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def reefshark(ctx):
    embed = discord.Embed(

        title="**Reef Shark**", description="\nShip made by Goldman."
    )
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/0b/Dolphin.png/revision/latest/scale-to-width-down/200?cb=20190903140304"
    )
    embed.add_field(
        name="Infos", value="Level: 5\nModel: 5\nMass: 200", inline=False
    )
    embed.add_field(name="Shield", value="Cap :  225/300\nRegen: 6/8", inline=False)
    embed.add_field(
        name="Energy",
        value=f"Cap :  250/300\nRegen :  50/80\nCannon damage/shot :  50/65 (1 lasers)",
        inline=False,
    )
    embed.add_field(name="Turning rate", value="90/110", inline=False)
    embed.add_field(name="Acceleration", value="90/120", inline=False)
    embed.add_field(name="Terminal Velocity", value="115/135", inline=False)
    
    await ctx.send(embed=embed)























@bot.command()
async def ships(ctx, modName, shipName):
    Type = str.lower(modName)
    Name = str.lower(shipName)
    if Type == "useries":
        if Name == "usniper":
            embed = discord.Embed(title= "**U-Sniper MK 2**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.")    
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/8c/U-Sniper_MK_2.png/revision/latest/scale-to-width-down/200?cb=20190312144514")
            embed.add_field(name= "Infos", value = "Level: 1\nModel: 1\nMass: 200", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/300\nRegen : 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 100/160\nRegen : 50/60\nCannon damage/shot : 80/120 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "125/145" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "ucruiser":
            embed = discord.Embed(title= "**U-Cruiser**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/3/36/U-Cruiser.png/revision/latest/scale-to-width-down/200?cb=20190312120419")
            embed.add_field(name= "Infos", value = "Level: 2\nModel: 1\nMass: 220", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/350\nRegen : 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 120/200\nRegen : 50/100\nCannon damage/shot : 120/160 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "50/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "110/130" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uquad":
            embed = discord.Embed(title= "**U-Quad**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/11/U-Quad.png/revision/latest/scale-to-width-down/200?cb=20190312142139")
            embed.add_field(name= "Infos", value = "Level: 2\nModel: 2\nMass: 320", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 210/340\nRegen : 6/10", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 160/320\nRegen : 80/100\nCannon damage/shot : 160/240 (4 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/60" , inline= False)
            embed.add_field(name= "Acceleration", value = "90/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/120" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "upenta":
            embed = discord.Embed(title= "**U-Penta**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/69/U-Penta.png/revision/latest/scale-to-width-down/200?cb=20190312120517")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 1\nMass: 400", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/350\nRegen : 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 300/450\nRegen : 150/300\nCannon damage/shot : 210/310 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/60" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/120" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uspread":
            embed = discord.Embed(title= "**U-Spread**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/68/U-Spread.png/revision/latest/scale-to-width-down/200?cb=20190312141923")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 2\nMass: 400", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 350/500\nRegen : 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 400/600\nRegen : 250/400\nCannon damage/shot : 320/460 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/60" , inline= False)
            embed.add_field(name= "Acceleration", value = "40/60" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/120" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "hwarrior":
            embed = discord.Embed(title= "**H-Warrior**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/18/H-Warrior.png/revision/latest/scale-to-width-down/200?cb=20190312131115")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 3\nMass: 220", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 220/320\nRegen : 5/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 180/250\nRegen : 75/100\nCannon damage/shot : 180/240 (4 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "110/130" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "usentry":
            embed = discord.Embed(title= "**U-Sentry**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/3/30/U-Sentry.png/revision/latest/scale-to-width-down/200?cb=20190312152105")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 4\nMass: 240", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 200/300\nRegen : 3/5", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 300/500\nRegen : 100/150\nCannon damage/shot : 80/120 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "30/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "70/120" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/110" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uarsenal":
            embed = discord.Embed(title= "**U-Arsenal**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/9c/U-Arsenal.png/revision/latest/scale-to-width-down/200?cb=20190312120613")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 1\nMass: 450", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/300\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 350/600\nRegen : 150/200\nCannon damage/shot : 280/420 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "30/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/110" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "ucenter":
            embed = discord.Embed(title= "**U-Center**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/c/c6/U-Center.png/revision/latest/scale-to-width-down/200?cb=20190312141750")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 2\nMass: 500", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 600/800\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 400/600\nRegen : 250/350\nCannon damage/shot : 440/560 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "20/40" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/150" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "70/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uinterceptor":
            embed = discord.Embed(title= "**U-Interceptor**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/de/U-Interceptor.png/revision/latest/scale-to-width-down/200?cb=20190312131241")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 4\nMass: 300", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/400\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 350/600\nRegen : 125/300\nCannon damage/shot : 140/240 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "35/45" , inline= False)
            embed.add_field(name= "Acceleration", value = "55/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "110/125" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uspeeder":
            embed = discord.Embed(title= "**U-Speeder**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/79/U-Speeder.png/revision/latest/scale-to-width-down/200?cb=20190312152150")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 5\nMass: 250", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 300/400\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 200/400\nRegen : 100/200\nCannon damage/shot : 140/200 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/120" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "usiege":
            embed = discord.Embed(title= "**U-Siege**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/6b/U-Siege.png/revision/latest/scale-to-width-down/200?cb=20190312152244")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 6\nMass: 250", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 220/350\nRegen : 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 450/650\nRegen : 75/150\nCannon damage/shot : 105/170 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "75/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "upunisher":
            embed = discord.Embed(title= "**U-Punisher**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/3/3b/U-Punisher.png/revision/latest/scale-to-width-down/200?cb=20190312120658")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 1\nMass: 250", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 350/500\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 350/600\nRegen : 75/150\nCannon damage/shot : 350/530 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "30/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "40/80" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "95/115" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uocta":
            embed = discord.Embed(title= "**U-Octa**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/59/U-Octa.png/revision/latest/scale-to-width-down/200?cb=20190312141827")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 2\nMass: 850", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 500/750\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 500/800\nRegen : 200/300\nCannon damage/shot : 310/470 (8 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/40" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/150" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "hdestroyer":
            embed = discord.Embed(title= "**H-Destroyer**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4e/H-Destroyer.png/revision/latest/scale-to-width-down/200?cb=20190312131544")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 3\nMass: 450", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 300/450\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 700/1100\nRegen : 90/200\nCannon damage/shot : 180/280 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "35/55" , inline= False)
            embed.add_field(name= "Acceleration", value = "85/120" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "trailblazer":
            embed = discord.Embed(title= "**Trailblazer**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/89/Trailblazer.png/revision/latest/scale-to-width-down/200?cb=20190312152340")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 4\nMass: 350", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 280/400\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 440/600\nRegen : 100/150\nCannon damage/shot : 250/400 (4 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/55" , inline= False)
            embed.add_field(name= "Acceleration", value = "40/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/125" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "udemon":
            embed = discord.Embed(title= "**U-Demon**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/b/b7/U-Demon.png/revision/latest/scale-to-width-down/200?cb=20190312152429")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 5\nMass: 350", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 280/400\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 440/700\nRegen : 80/120\nCannon damage/shot : 300/560 (6 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "60/80" , inline= False)
            embed.add_field(name= "Acceleration", value = "90/140" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/114" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "upulsar":
            embed = discord.Embed(title= "**U-Pulsar**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/7c/U-Pulsar.png/revision/latest/scale-to-width-down/200?cb=20190312152518")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 6\nMass: 300", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/400\nRegen : 6/12", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 500/750\nRegen : 80/160\nCannon damage/shot : 150/300 (30 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "ubarricade":
            embed = discord.Embed(title= "**U-Barricade**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/3/38/U-Barricade.png/revision/latest/scale-to-width-down/200?cb=20190312120759")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 1\nMass: 700", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 450/600\nRegen : 15/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 500/800\nRegen : 100/175\nCannon damage/shot : 470/710 (12 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "15/20" , inline= False)
            embed.add_field(name= "Acceleration", value = "20/55" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/120" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "umonitor":
            embed = discord.Embed(title= "**U-Monitor**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/6c/U-Monitor.png/revision/latest/scale-to-width-down/200?cb=20190312142018")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 2\nMass: 700", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 350/500\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 550/700\nRegen : 350/450\nCannon damage/shot : 590/650 (13 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "20/30" , inline= False)
            embed.add_field(name= "Acceleration", value = "50/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uperimeter":
            embed = discord.Embed(title= "**U-Perimeter**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/9a/U-Perimeter.png/revision/latest/scale-to-width-down/200?cb=20190312131701")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 3\nMass: 900", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 650/900\nRegen : 10/25", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 750/1100\nRegen : 250/300\nCannon damage/shot : 660/880 (12 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "20/40" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/150" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/95" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "ubruiser":
            embed = discord.Embed(title= "**U-Bruiser**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/14/U-Bruiser.png/revision/latest/scale-to-width-down/200?cb=20190312131835")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 4\nMass: 700", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 425/700\nRegen : 10/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 400/800\nRegen : 140/200\nCannon damage/shot : 320/520 (8 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "25/45" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/120" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "55/85" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uafterburn":
            embed = discord.Embed(title= "**U-Afterburn**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/2/2a/U-Afterburn.png/revision/latest/scale-to-width-down/200?cb=20190312152612")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 5\nMass: 250", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 300/500\nRegen : 15/40", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 600/800\nRegen : 100/150\nCannon damage/shot : 330/420 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "45/60" , inline= False)
            embed.add_field(name= "Acceleration", value = "40/80" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "110/130" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "usmasher":
            embed = discord.Embed(title= "**U-Smasher**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/41/U-Smasher.png/revision/latest/scale-to-width-down/200?cb=20190312152701")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 6\nMass: 700", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 600/800\nRegen : 20/35", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 400/600\nRegen : 30/80\nCannon damage/shot : 140/80 (6 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "15/25" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/120" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "hellfire":
            embed = discord.Embed(title= "**Hellfire**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4e/Hellfire.png/revision/latest/scale-to-width-down/200?cb=20190312152746")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 7\nMass: 500", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 400/550\nRegen : 10/15", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 400/800\nRegen : 100/120\nCannon damage/shot : 60/90 (6 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "30/40" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/80" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "70/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "u10thunder":
            embed = discord.Embed(title= "**U-10 Thunder**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/95/U-10_Thunder.png/revision/latest/scale-to-width-down/200?cb=20190312152838")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 8\nMass: 400", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 300/500\nRegen : 10/15", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 600/950\nRegen : 100/200\nCannon damage/shot : 80/120 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "70/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "uwall":
            embed = discord.Embed(title= "**U-Wall**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/a/a6/U-Wall.png/revision/latest/scale-to-width-down/200?cb=20190312120912")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 1\nMass: 800", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 800/800\nRegen : 20/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 3500/3500\nRegen : 700/700\nCannon damage/shot : 1200/1200 (64 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "10/10" , inline= False)
            embed.add_field(name= "Acceleration", value = "110/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "110/110" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "hearthbreaker":
            embed = discord.Embed(title= "**Heartbreaker**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/8e/Heartbreaker.png/revision/latest/scale-to-width-down/200?cb=20190312152920")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 2\nMass: 600", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 800/800\nRegen : 15/15", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 6000/600\nRegen : 700/700\nCannon damage/shot : 2880/2880 (37 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "70/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "90/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "ufusion":
            embed = discord.Embed(title= "**U-Fusion**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/7a/U-Fusion-current.png/revision/latest/scale-to-width-down/200?cb=20200411041422")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 3\nMass: 1200", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 800/800\nRegen : 20/20", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 1600/1600\nRegen : 200/200\nCannon damage/shot : 760/760 (21 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "10/10" , inline= False)
            embed.add_field(name= "Acceleration", value = "150/150" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "50/50" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "umarksman":
            embed = discord.Embed(title= "**U-Marksman**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/d7/U-Marksman.png/revision/latest/scale-to-width-down/200?cb=20190312153108")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 4\nMass: 800", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 500/500\nRegen : 12/12", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 800/800\nRegen : 95/95\nCannon damage/shot : 601/601 (25 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/60" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "125/125" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "shadowx27":
            embed = discord.Embed(title= "**Shadow X-27**", description= f"asked by {ctx.message.author.mention}\nShip made by Finalizer.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/d7/U-Marksman.png/revision/latest/scale-to-width-down/200?cb=20190312153108")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 5\nMass: 400", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 600/600\nRegen : 10/10", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 1000/1000\nRegen : 200/200\nCannon damage/shot : 900/900 (90 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "110/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/+0" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "list":
            embed = discord.Embed(title="**U-Series ships:**",description ="\nTier 1: U-Sniper MK2\nTier 2: U-Cruiser, U-Quad\nTier 3: U-Penta, U-Spread, H-Warrior, U-Sentry\nTier 4: U-Arsenal, U-Center, U-Interceptor, U-Speeder, U-Siege\nTier 5: U-Punisher, U-Octa, H-Destroyer, Traiblazer, U-Demon, U-Pulsar\nTier 6: U-Barricade, U-Monitor, U-Perimeter, U-Bruiser, U-Afterburn, U-Smasher, Hellfire, U-10 Thunder\nTier 7: U-Wall, Heartbreaker, U-Fusion, U-Marksman, Shadow X-27\n\n\nIf you want more information about a ship, type `o,TheShipYouWant`.")
            embed.set_thumbnail(url="https://starblastio.gamepedia.com/File:Useries.jpg")
            await ctx.send(embed = embed)
    elif Type == "alienintrusion":
        if Name == "fly" or Name == "flyv2":
            embed = discord.Embed(title= "**Fly V2**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/1e/Fly_V2.png/revision/latest/scale-to-width-down/200?cb=20190915001145")
            embed.add_field(name= "Infos", value = "Level: 1\nModel: 1\nMass: 60", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 75/100\nRegen: 2/3", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 75/100\nRegen : 20/28\nCannon damage/shot : 10/14 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "110/130" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/120" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "125/145" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "lightfighter":
            embed = discord.Embed(title= "**Light-Fighter**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/16/Light-Fighter.png/revision/latest/scale-to-width-down/200?cb=20190915001206")
            embed.add_field(name= "Infos", value = "Level: 2\nModel: 1\nMass: 90", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 100/150\nRegen: 3/5", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 75/100\nRegen : 30/40\nCannon damage/shot : 10/15 (1 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "100/130" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/130" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/115" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "atom":
            embed = discord.Embed(title= "**Atom**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/1b/Atom.png/revision/latest/scale-to-width-down/200?cb=20190915001232")
            embed.add_field(name= "Infos", value = "Level: 2\nModel: 2\nMass: 105", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 125/175\nRegen: 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 100/125\nRegen : 25/30\nCannon damage/shot : 10/14 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "70/95" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/115" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/105" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "angelwing":
            embed = discord.Embed(title= "**Angel-Wing**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/1d/Angel_Wing.png/revision/latest/scale-to-width-down/200?cb=20190915001336")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 2\nMass: 150", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 125/200\nRegen: 3/5", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 100/150\nRegen : 35/50\nCannon damage/shot : 10/18 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "65/90" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/120" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "120/135" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "pegasus":
            embed = discord.Embed(title= "**Pegasus**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4a/Pegasus.png/revision/latest/scale-to-width-down/200?cb=20190915001316")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 1\nMass: 170", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 150/225\nRegen: 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 90/125\nRegen : 30/45\nCannon damage/shot : 34/50 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "35/55" , inline= False)
            embed.add_field(name= "Acceleration", value = "50/80" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/110" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "cayman":
            embed = discord.Embed(title= "**Cayman**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/8d/Cayman.png/revision/latest/scale-to-width-down/200?cb=20190915001401")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 3\nMass: 200", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 150/225\nRegen: 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 100/135\nRegen : 33/43\nCannon damage/shot : 29/40 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "65/80" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "75/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "hammer":
            embed = discord.Embed(title= "**Hammer**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/81/Hammer.png/revision/latest/scale-to-width-down/200?cb=20190915001432")
            embed.add_field(name= "Infos", value = "Level: 3\nModel: 4\nMass: 235", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 175/250\nRegen: 5/7", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 75/120\nRegen : 20/25\nThis ship use a dash: 35/55 damages", inline= False)
            embed.add_field(name= "Turning rate", value = "40/55" , inline= False)
            embed.add_field(name= "Acceleration", value = "95/125" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "95/110" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "dragonfly":
            embed = discord.Embed(title= "**Dragonfly**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/8/84/Dragonfly.png/revision/latest/scale-to-width-down/200?cb=20190915001528")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 1\nMass: 180", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 175/250\nRegen: 4/7", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 100/150\nRegen : 45/60\nCannon damage/shot : 59/82 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "65/80" , inline= False)
            embed.add_field(name= "Acceleration", value = "90/115" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "85/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "stingray":
            embed = discord.Embed(title= "**Stingray**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/7/7a/Stingray_%28Intrusion_%26_Battle_Royale%29.png/revision/latest/scale-to-width-down/200?cb=20190915001554")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 2\nMass: 200", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 175/250\nRegen: 4/7", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 125/175\nRegen : 45/60\nCannon damage/shot : 44/54 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "65/80" , inline= False)
            embed.add_field(name= "Acceleration", value = "90/130" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "95/110" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "azimuth":
            embed = discord.Embed(title= "**Azimuth**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/e/e5/Azimuth.png/revision/latest/scale-to-width-down/200?cb=20190915001610")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 3\nMass: 200", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 200/275\nRegen: 4/7", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 125/150\nRegen : 35/50\nCannon damage/shot : 14/21 (1 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "65/80" , inline= False)
            embed.add_field(name= "Acceleration", value = "65/85" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "85/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "flashstar":
            embed = discord.Embed(title= "**Flash-Star**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/47/Flash_Star.png/revision/latest/scale-to-width-down/200?cb=20190915001657")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 4\nMass: 185", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 175/250\nRegen: 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 150/225\nRegen : 55/75\nCannon damage/shot : 37/54 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/125" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/105" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "trex":
            embed = discord.Embed(title= "**T-Rex**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/f8/T-Rex.png/revision/latest/scale-to-width-down/200?cb=20190915001722")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 5\nMass: 190", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 200/250\nRegen: 5/7", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 150/200\nRegen : 50/65\nCannon damage/shot : 28/39 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "55/75" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/130" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "hconqueror":
            embed = discord.Embed(title= "**H Conqueror**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/a/af/H_Conqueror.png/revision/latest/scale-to-width-down/200?cb=20190915001741")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 6\nMass: 200", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 200/275\nRegen: 4/6", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 150/200\nRegen : 45/60\nCannon damage/shot : 48/63 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "35/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "70/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "mdefender":
            embed = discord.Embed(title= "**M-Defender**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/c/ca/M-Defender.png/revision/latest/scale-to-width-down/200?cb=20190915001810")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 7\nMass: 225", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 225/300\nRegen: 5/7", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 125/175\nRegen : 35/48\nCannon damage/shot : 50/70 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/55" , inline= False)
            embed.add_field(name= "Acceleration", value = "70/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "simuran":
            embed = discord.Embed(title= "**Simuran**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/1a/Simuran.png/revision/latest/scale-to-width-down/200?cb=20190915001845")
            embed.add_field(name= "Infos", value = "Level: 4\nModel: 8\nMass: 225", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 225/300\nRegen: 5/7", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 125/175\nRegen : 40/55\nCannon damage/shot : 35/45 (1 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "75/85" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "atlant":
            embed = discord.Embed(title= "**Atlant**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/9c/Atlant.png/revision/latest/scale-to-width-down/200?cb=20190915001934")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 1\nMass: 250", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/325\nRegen: 6/9", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 150/200\nRegen : 65/80\nCannon damage/shot : 84/112 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "60/75" , inline= False)
            embed.add_field(name= "Acceleration", value = "105/135" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "75/85" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "vortex":
            embed = discord.Embed(title= "**Vortex**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/52/Vortex.png/revision/latest/scale-to-width-down/200?cb=20190915001949")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 2\nMass: 265", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 150/300\nRegen: 5/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 200/250\nRegen : 65/90\nCannon damage/shot : 70/100 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "55/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "90/125" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "70/80" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "deltaspeedster":
            embed = discord.Embed(title= "**Dela-Speedster**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/00/DeltaSpeedster.png/revision/latest/scale-to-width-down/200?cb=20190914193203")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 3\nMass: 185", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/350\nRegen: 6/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 175/250\nRegen : 50/75\nCannon damage/shot : 91/125 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "85/110" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/125" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "105/120" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "hawk":
            embed = discord.Embed(title= "**Hawk**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/3/3c/Hawk.png/revision/latest/scale-to-width-down/200?cb=20190915002014")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 4\nMass: 210", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/350\nRegen: 6/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 225/300\nRegen : 65/90\nCannon damage/shot : 32/54 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "75/100" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/125" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "100/115" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "photon":
            embed = discord.Embed(title= "**Photon**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/51/Photon.png/revision/latest/scale-to-width-down/200?cb=20190915002039")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 5\nMass: 190", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/325\nRegen: 6/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 175/250\nRegen : 65/90\nCannon damage/shot : 27/34 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "35/50" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/80" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "125/140" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "varan":
            embed = discord.Embed(title= "**Varan**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/c/c8/Varan.png/revision/latest/scale-to-width-down/200?cb=20190915002104")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 6\nMass: 220", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 250/350\nRegen: 5/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 225/300\nRegen : 90/115\nCannon damage/shot : 28/44 (4 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "60/80" , inline= False)
            embed.add_field(name= "Acceleration", value = "75/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "83/93" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "spark":
            embed = discord.Embed(title= "**Spark**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/c/cd/Spark.png/revision/latest/scale-to-width-down/200?cb=20190915002124")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 7\nMass: 250", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/375\nRegen: 6/9", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 250/325\nRegen : 70/95\nCannon damage/shot : 34/64 (4 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "60/80" , inline= False)
            embed.add_field(name= "Acceleration", value = "65/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "85/95" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "predator":
            embed = discord.Embed(title= "**Predator**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/e/e9/Predator.png/revision/latest/scale-to-width-down/200?cb=20190915002145")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 8\nMass: 300", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/375\nRegen: 6/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 200/275\nRegen : 50/90\nCannon damage/shot : 54/70 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/55" , inline= False)
            embed.add_field(name= "Acceleration", value = "75/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "vampire":
            embed = discord.Embed(title= "**Vampire**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/4/4e/Vampire.png/revision/latest/scale-to-width-down/200?cb=20190915002205")
            embed.add_field(name= "Infos", value = "Level: 5\nModel: 9\nMass: 350", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 350/450\nRegen: 7/9", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 150/225\nRegen : 45/60\nCannon damage/shot : 35/50 (1 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/55" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "berserk":
            await ctx.send('To do.')
        elif Name == "leviathan":
            embed = discord.Embed(title= "**Leviathan**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/0a/Leviathan.png/revision/latest/scale-to-width-down/200?cb=20190915002248")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 1\nMass: 280", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/375\nRegen: 7/9", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 325/400\nRegen : 70/110\nCannon damage/shot : 119/188 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "85/110" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "75/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "sidedestroyer":
            embed = discord.Embed(title= "**Side-Destroyer**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/e/e6/Side-Destroyer.png/revision/latest/scale-to-width-down/200?cb=20190915002350")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 2\nMass: 275", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 300/400\nRegen: 8/10", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 350/450\nRegen : 125/150\nCannon damage/shot : 160/212 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/95" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "falcon":
            embed = discord.Embed(title= "**Flacon**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/0/06/Falcon.png/revision/latest/scale-to-width-down/200?cb=20190915002404")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 3\nMass: 265", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/375\nRegen: 7/9", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 300/400\nRegen : 105/150\nCannon damage/shot : 108/153 (6 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "70/90" , inline= False)
            embed.add_field(name= "Acceleration", value = "85/105" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "90/100" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "helius":
            embed = discord.Embed(title= "**Helius**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/98/Helius.png/revision/latest/scale-to-width-down/200?cb=20190914201636")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 4\nMass: 325", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 275/350\nRegen: 6/8", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 225/300\nRegen : 85/105\nCannon damage/shot : 80/120 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/65" , inline= False)
            embed.add_field(name= "Acceleration", value = "75/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/95" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "phoenix":
            embed = discord.Embed(title= "**Phoenix**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/c/c1/Phoenix.png/revision/latest/scale-to-width-down/200?cb=20190915002424")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 5\nMass: 255", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 200/325\nRegen: 7/9", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 325/450\nRegen : 85/105\nCannon damage/shot : 32/54 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "110/130" , inline= False)
            embed.add_field(name= "Acceleration", value = "100/120" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "105/125" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "harpy":
            embed = discord.Embed(title= "**Harpy**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/1/1b/Harpy.png/revision/latest/scale-to-width-down/200?cb=20190915002440")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 6\nMass: 260", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 200/300\nRegen: 7/9", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 300/425\nRegen : 75/100\nCannon damage/shot : 20/28 (4 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "105/125" , inline= False)
            embed.add_field(name= "Acceleration", value = "95/115" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "115/130" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "wwarrior":
            embed = discord.Embed(title= "**W-Warrior**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/fa/W-Warrior.png/revision/latest/scale-to-width-down/200?cb=20190915002500")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 7\nMass: 365", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 325/425\nRegen: 8/11", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 300/450\nRegen : 95/135\nCannon damage/shot : 42/60 (6 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "60/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "85/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/95" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "goliath":
            embed = discord.Embed(title= "**Goliath**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/e/e5/Goliath.png/revision/latest/scale-to-width-down/200?cb=20190915002519")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 8\nMass: 400", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 350/500\nRegen: 9/13", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 300/400\nRegen : 85/110\nCannon damage/shot : 45/60 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "75/120" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/95" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "centurion":
            embed = discord.Embed(title= "**Centurion**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/5/5d/Centurion.png/revision/latest/scale-to-width-down/200?cb=20190915002543")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 9\nMass: 400", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 300/500\nRegen: 8/11", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 350/425\nRegen : 110/135\nCannon damage/shot : 50/80 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "45/75" , inline= False)
            embed.add_field(name= "Acceleration", value = "70/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "85/95" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "prometheus":
            embed = discord.Embed(title= "**Prometheus**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/6/63/Prometheus.png/revision/latest/scale-to-width-down/200?cb=20190915002604")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 10\nMass: 480", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 300/500\nRegen: 8/11", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 325/425\nRegen : 100/135\nCannon damage/shot : 91/124 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "50/70" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "80/90" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "chronos":
            embed = discord.Embed(title= "**Chronos**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/94/Chronos.png/revision/latest/scale-to-width-down/200?cb=20190915002621")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 11\nMass: 490", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 400/575\nRegen: 9/12", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 300/375\nRegen : 90/120\nCannon damage/shot : 130/180 (2 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "45/60" , inline= False)
            embed.add_field(name= "Acceleration", value = "75/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "70/85" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "cthulhu":
            embed = discord.Embed(title= "**Cthulhu**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/9/9e/Cthulhu.png/revision/latest/scale-to-width-down/200?cb=20190915002647")
            embed.add_field(name= "Infos", value = "Level: 6\nModel: 12\nMass: 550", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 425/600\nRegen: 10/13", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 200/275\nRegen : 70/95\nCannon damage/shot : 70/90 (1 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "45/60" , inline= False)
            embed.add_field(name= "Acceleration", value = "75/100" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "65/80" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "vdestroyer":
            embed = discord.Embed(title= "**V-Destroyer**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/f1/V-Destroyer.png/revision/latest/scale-to-width-down/200?cb=20190915002706")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 1\nMass: 700", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 700/700\nRegen: 15/15", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 375/375\nRegen : 150/150\nCannon damage/shot : 325/325 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "32/32" , inline= False)
            embed.add_field(name= "Acceleration", value = "80/80" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "60/60" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "waspspiner":
            embed = discord.Embed(title= "**Wasp Sniper**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/a/af/WaspSniper.png/revision/latest/scale-to-width-down/200?cb=20190914204309")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 2\nMass: 400", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 450/450\nRegen: 10/10", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 400/400\nRegen : 100/100\nCannon damage/shot : 282/282 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "40/40" , inline= False)
            embed.add_field(name= "Acceleration", value = "60/60" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "130/130" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "miles":
            embed = discord.Embed(title= "**Miles**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/a/a8/Miles.png/revision/latest/scale-to-width-down/200?cb=20190915002731")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 3\nMass: 500", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 550/550\nRegen: 14/14", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 500/500\nRegen : 110/110\nCannon damage/shot : 40/40 (4 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "60/60" , inline= False)
            embed.add_field(name= "Acceleration", value = "70/70" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "85/85" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "himera":
            embed = discord.Embed(title= "**Himera**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/d/d9/Himera.png/revision/latest/scale-to-width-down/200?cb=20190915002749")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 4\nMass: 550", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 550/550\nRegen: 16/16", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 600/600\nRegen : 175/175\nCannon damage/shot : 144/144 (5 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "25/25" , inline= False)
            embed.add_field(name= "Acceleration", value = "90/90" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "70/70" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "chronosr35":
            embed = discord.Embed(title= "**Chronos R35**", description= f"asked by {ctx.message.author.mention}\nShip made by Goldman.") 
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/starblastio_gamepedia_en/images/f/f9/Chronos_R35.png/revision/latest/scale-to-width-down/200?cb=20190915002806")
            embed.add_field(name= "Infos", value = "Level: 7\nModel: 5\nMass: 800", inline = False)
            embed.add_field(name= "Shield", value = "Cap : 750/750\nRegen: 18/18", inline= False )
            embed.add_field(name= "Energy", value = "Cap : 425/425\nRegen : 100/100\nCannon damage/shot : 250/250 (3 lasers)", inline= False)
            embed.add_field(name= "Turning rate", value = "20/20" , inline= False)
            embed.add_field(name= "Acceleration", value = "55/55" , inline= False)
            embed.add_field(name= "Terminal Velocity", value = "40/40" , inline= False)
            
            await ctx.send(embed = embed)
        elif Name == "list":
            embed = discord.Embed(title="**Alien Intrusion ships:**", description ="\nTier 1: Fly V2\nTier 2: Light-Fighter, Atom\nTier 3: Pegasus, Angel Wing, Cayman, Hammer\nTier 4: Dragonfly, Stingray, Azimuth, Flash Star, T-Rex, H Conqueror, M-Defender, Simuran\nTier 5: Atlant, Vortex, Delta Speedster, Hawk, Photon, Varan, Spark, Predator, Vampire, Berserk\nTier 6: Leviathan, Side-Destroyer, Falcon, Helius, Phoenix, Harpy, W-Warrior, Goliath, Centurion, Prometheus, Chronos, Cthulhu\nTier 7: V-Destroyer, Wasp Sniper, Miles, Himera, Chronos R35\n\nRemoved ships: Squid, Typhoon, Bee Sniper\n\n\nIf you want more information about a ship, type `o,TheShipYouWant`. ")
            embed.set_thumbnail(url="https://starblastio.gamepedia.com/File:AlienIntrusion5.0Banner.PNG")
            await ctx.send(embed = embed)








bot.run("") 
