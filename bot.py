#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv
import discord
import random
import re
import terning

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

current_rules_id = 0
rules = terning.load_rules(current_rules_id)

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
        response = terning.pretty_rules(rules, current_rules_id)
        await message.channel.send(response)

    if message.content == '!save':
        response = terning.save_rules(rules, current_rules_id)
        await message.channel.send(response)

    if message.content[:5] == '!load' and message.content[6:].replace(" ", "").isnumeric():
        current_rules_id = int(message.content[6:].replace(" ", ""))
        response = terning.load_rules(current_rules_id)
        await message.channel.send(response)

client.run(TOKEN)
