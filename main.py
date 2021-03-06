# bot.py
import os, glob, datetime, time

import discord
from discord.ext import commands, tasks
import logging

from SECRET import TOKEN, GUILD
from commands import COMMANDS
from modules.covid.covid import robot_export

COVID_DAILY_DONE = False
COVID_TIME = 9
covid_wait = time.time()

logging.basicConfig(filename='bot.log', format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)

client = discord.Client()


# @tasks.loop(seconds=60)
# async def covid():
#     global covid_wait
#     now = datetime.datetime.now()
#     if COVID_TIME == now.hour and time.time() > covid_wait:
#         covid_wait = time.time() + 3600 + 100
#         msg = robot_export()
#         for channel in client.get_all_channels():
#             if channel.name.endswith("covid"):
#                 for filepath in glob.glob("figs/covid_*.png"):
#                     await channel.send(file=discord.File(str(filepath)))
#                 await channel.send(msg)


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

        msg = "CALL | User: {} | call: {} ".format(message.author, message.content)
        logging.info(msg)

        if command in COMMANDS:
            response = COMMANDS[command](params)
            for line in response:
                if line["type"] == "text":
                    await message.channel.send(line["text"])
                elif line["type"] == "fig":
                    await message.channel.send(file=discord.File(line["filepath"]))

    else:
        return

# covid.start()
client.run(TOKEN)
