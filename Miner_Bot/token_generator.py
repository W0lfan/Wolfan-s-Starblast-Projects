import string
import random 

class token:
    async def create(channel,bot):
        letters = list(string.ascii_lowercase)
        token = []
        for i in range(0,21):
            if random.randint(0,1) == 0: # => Letter
                token.append(str(letters[random.randrange(27)]))
            else:
                token.append(str(random.randint(0,9)))
        channel = bot.get_channel(channel)
        message = ''.join([str(elem) for elem in token])
        await channel.send(f"**NEW MAP**\n`Token` : {message}")