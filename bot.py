#!/usr/bin/env python3

import requests

troll = "https://topps.diku.dk/torbenm/troll.msp"

data = { 'selectExp' : '',
         'userExp' : '',
         'trollExp' : '1d20',
         'what' : 'Make+random+rolls',
         'noOfDice' : '1',
         'precision' : '',
         'col2' : 'ge',
         'multiplier' : '',
         'mailAddr' : '',
         'mailSubj' : '',
         'captchaCode' : '788879',
         'captchaGiven' : '',
         'description' : '' }

test = requests.post(troll, data=data)

print(test.text)

