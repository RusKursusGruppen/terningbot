#!/usr/bin/env python3

import requests

troll = "https://topps.diku.dk/torbenm/troll.msp"

data = { 'what' : 'Make random rolls.',
         'trollExp' : '1d20',
         'noOfDice' : '1'
        }

test = requests.post(troll, data=data)

print(test.text)

