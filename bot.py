#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv
import discord
import random
import re


troll = "https://topps.diku.dk/torbenm/troll.msp"

data = { 'what' : 'Make random rolls.',
         'trollExp' : '1d20',
         'noOfDice' : '1'
        }

def make_roll():
    test = requests.post(troll, data=data)

    for line in test.text.split('\n'):
        if '<P>Rolls' in line:
            return re.sub("[^0-9]", "", line.split()[-1])

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

client = discord.Client()

rules = [""] * 20

rules[0] = "Tag 1 bunder!"
rules[1] = "Tag 1/2 bunder!"
rules[10] = "Lav en ny regel"
rules[18] = "Giv 1/2 bunder!"
rules[19] = "Giv 1 bunder!"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!r':
        response = make_roll()
        rule = rules[int(response)-1]
        await message.channel.send(response)
        if rule == "":
            await message.channel.send("Lav en ny regel!")
        else: 
            await message.channel.send(rule)
           

    if message.content == '!rules':
        response = make_roll()
        await message.channel.send(response)

    if message.content == '!save':
        response = make_roll()
        await message.channel.send(response)

    if message.content == '!load':
        response = make_roll()
        await message.channel.send(response)


client.run(TOKEN)
