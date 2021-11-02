# bot.py
import os

import discord

from SECRET import TOKEN, GUILD
from commands import COMMANDS



client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    for command in COMMANDS:
        if command.startswith(message.content):
            response = COMMANDS[command](message.content)
            for line in response:
                if line["type"] == "text":
                    await message.channel.send(line["text"])
                elif line["type"] == "fig":
                    await message.channel.send(file=discord.File(line["filepath"]))



    else:
        return


client.run(TOKEN)
