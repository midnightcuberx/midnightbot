const Discord = require("discord.js")
const client = new Discord.Client();
const fs = require('fs')
const prefix="m!"
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
client.commands = new Discord.Collection()
for (const file of commandFiles) {
    const command = require(`./commands/${file}`);
    client.commands.set(command.name, command);
}
client.on('message', message => {
    if (!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(" ");
    const command = args.shift().toLowerCase();

    if (!client.commands.has(command)) return;

try {
    client.commands.get(command).execute(client, message, args);
} 
catch (error) {
    message.channel.send(error);
}
});
client.on('ready', async() => {

    console.log("Bot is Ready")
});

const keepAlive = require('./server');
keepAlive();
client.login(token)
