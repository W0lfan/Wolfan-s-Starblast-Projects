const Discord = require("discord.js");
const Client = new Discord.Client;


Client.on("ready",() => {
    console.log("Bot started.")
})
Client.on("message", function(message){
    const channel = message.channel;
    const user = message.author;
    if (user.id !== Client.user.id) {
        if (channel.name === "tests" || channel.name === "game-links") {
            var message_content = message.content;
            var messages = [];
            var z = [];
            var l = ' ';
            var length = 0;
            var word = 'https://starblast.io/';
            if (message_content.includes(word) === true) {
                z = message_content.split(' ');
                for (let i in z) {
                    if (z[i].includes("https://starblast.io/") === true) {
                        l = z[i].replace("https://starblast.io/",'');
                        l = l.replace('#','');
                        length = l.length
                    }
                }
                if (l.includes('@') === true && l.includes(':') === true && l.includes('.') === true) {
                    if (isNaN(l)) {
                        channel.send(`<@${message.author.id}> please use correct game links: they must be a number (for example #20).\nYour message has been deleted and sent to you for your conveniance.`);
                        user.send(message_content);
                        message.delete();
                    }
                } 
                else if (length > 4) {
                    channel.send(`<@${message.author.id}> please use correct game links: they must be a number with less than 4 characters.\nYour message has been deleted and sent to you for your conveniance.`)
                    user.send(message_content);
                    message.delete();
                }
                takeHistory = function (limit) {
                    return new Promise(function (resolve, reject) {
                      message.channel.fetch(true).then(channel => resolve([...channel.messages.cache].map(i => i[1]).slice(-limit).reverse())).catch(reject)
                    })
                  }
                takeHistory(11).then(messages => messages.forEach(message => console.log(message.content)));
            }
        }
    }
});



/*
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
*/
Client.login('')
