# bot.py
import os

import discord
from discord.ext import commands, tasks

from SECRET import TOKEN, GUILD
from commands import COMMANDS
from modules.covid.covid import make_covid_report_when_new

client = discord.Client()


@tasks.loop(seconds=15)
async def covid():
    if make_covid_report_when_new():
        for channel in client.get_all_channels():
            if channel.name.endswith("test"):
                filepath = os.path.join("modules", "covid", "figs", "plot1.png")
                await channel.send("test")
                await channel.send(file=discord.File(filepath))



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

    if message.content.startswith("\\"):
        cells = message.content.split(" ")
        command = cells[0]
        if len(cells) > 1:
            params =  " ".join(message.content.split(" ")[1:])
        else:
            params = ""

        if command in COMMANDS:
            response = COMMANDS[command](params)
            for line in response:
                if line["type"] == "text":
                    await message.channel.send(line["text"])
                elif line["type"] == "fig":
                    await message.channel.send(file=discord.File(line["filepath"]))

    else:
        return

covid.start()
client.run(TOKEN)
