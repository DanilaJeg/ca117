#!/usr/bin/env python3

import sys

table = sys.stdin.readlines()

longest = 0
for team in table:
    team = " ".join(team.split()[1:-8])
    if len(team) > longest:
        longest = len(team)

print(f'{"POS":>3} {"CLUB":{longest}} {"P":>2} {"W":>3} {"D":>3} {"L":>3} {"GF":>3} {"GA":>3} {"GD":>3} {"PTS":>3}')

for line in table:
    tokens = line.split()
    print(f'{tokens[0]:>3} {" ".join(tokens[1:-8]):{longest}} {tokens[-8]:>2} {tokens[-7]:>3} {tokens[-6]:>3} {tokens[-5]:>3} {tokens[-4]:>3} {tokens[-3]:>3} {tokens[-2]:>3} {tokens[-1]:>3}')
    
