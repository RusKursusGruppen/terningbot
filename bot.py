#!/usr/bin/env python3

import requests
import os

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

TOKEN = 'Nzg5NTA3OTY0NTI3NzA2MTIz.X9zElw.jHj41OF6Y6UiIJ5sjaKVpywXpww'
GUILD = 'terningtest'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!r':
        response = make_roll()
        await message.channel.send(response)

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
