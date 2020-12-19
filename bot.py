#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv
import discord
import random
import re
import json
import os.path

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

def save_rules(rule_set, rules_id):
    rules_file = "rules" + str(rules_id) + ".json"
    with open(rules_file, "w+") as f:
        json.dump(rule_set, f)

def load_rules(rules_id, new_game=False):
    rules_file = "rules" + str(rules_id) + ".json"
    if os.path.isfile(rules_file) and (not new_game):
        with open(rules_file, "r") as f:
            return json.load(f)
    else:
        rule_set = [""]*20
        rule_set[0] = "Tag 1 bunder!"
        rule_set[1] = "Tag 1/2 bunder!"
        rule_set[9] = "Lav en ny regel!"
        rule_set[18] = "Giv 1/2 bunder!"
        rule_set[19] = "Giv 1 bunder!"
        return rule_set

def pretty_rules(rule_set, rules_id):
    title = "Terning Rules - Rules-ID=" + str(rules_id) + " - \n"
    sep_line = ("#"*len(title)) + "\n"
    str_rules = ""
    for i in range(len(rule_set)):
        str_rules += "Rule " + str(i+1) + ": " + rule_set[i] + "\n"
    return title + sep_line + str_rules

current_rules_id = 0
rules = load_rules(current_rules_id)
# rules[0] = "Tag 1 bunder!"
# rules[1] = "Tag 1/2 bunder!"
# rules[9] = "Lav en ny regel"
# rules[18] = "Giv 1/2 bunder!"
# rules[19] = "Giv 1 bunder!"
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!r':
        response = make_roll()
        idx = int(response)-1
        rule = rules[idx]
        def check(reaction):
            return reaction.author == message.author or reaction == "skip"
        await message.channel.send(response)
        if rule == "":
            await message.channel.send("Lav en ny regel!")
            await message.channel.send(message.author)
            msg = await client.wait_for('message', timeout=200.0, check=check)
            rules[idx] = msg.content
        else:
            await message.channel.send(rule)
            if idx == 9:
                await message.channel.send(pretty_rules(rules, current_rules_id)) 
                await message.channel.send("vælg et tal")
                # test = await client.wait_for('message', timeout=200.0, check=check)
                while True:
                    test = await client.wait_for('message', timeout=200.0, check=check)
                    if test.content == "skip":
                        break
                    if (test.content.isnumeric()):
                        idx = int(test.content)-1
                    else:
                        await message.channel.send("idiot! der blev sagt et tal")
                        continue
                    if (idx >= 0 or idx < 20) and idx != 9:
                       break
                    else:
                        await message.channel.send("vælg et tal mellem 0 og 20, du kan ikke vælge 10")
                    
                if test.content == "skip":
                    await message.channel.send("næstes tur")
                else:
                    await message.channel.send("skriv din regel")
                    msg = await client.wait_for('message', timeout=200.0, check=check)
                    rules[idx] = msg.content
                

    if message.content == '!rules':
        response = pretty_rules(rules, current_rules_id)
        await message.channel.send(response)

    if message.content == '!save':
        terning.save_rules(rules, current_rules_id)
        response = "Saved rules-ID " + str(current_rules_id)
        await message.channel.send(response)

    cont = message.content.split(" ", 2)
    if len(cont) == 3:
        if cont[0] == "!c" and cont[1].isnumeric():
            rule = int(cont[1])-1
            if 0 <= rule and rule <= 20:
                prev_rule = rules[rule]
                rules[rule] = cont[2]
                response = "Change rule " + str(rule) + " from " + prev_rule + " to " + rules[rule]
                await message.channel.send(response)
    # if message.content[:5] == '!load' and message.content[6:].replace(" ", "").isnumeric():
    #     terning.save_rules(rules, current_rules_id)
    #     current_rules_id = int(message.content[6:].replace(" ", ""))
    #     rules = terning.load_rules(current_rules_id)
    #     response = "loaded rules-ID " + str(current_rules_id)
    #     await message.channel.send(response)

    # with message.content.split(" ", 2) as cont:
    #     response = "Wrong input"
    #     print(cont)
    #     if cont[0] == "!c" and cont[1].isnumeric:
    #         rule = int(cont[1])-1
    #         if 0 <= rule and rule <= 20:
    #             prev_rule = rules[rule]
    #             rules[rule] = cont[2]
    #             response = "Change rule " + str(rule) + " from " + prev_rule + " to " + rules[rule]
    #     await message.channel.send(response)


client.run(TOKEN)
