#!/usr/bin/env python3

import sys

def cupmove(move, cups):
    if move == "A":
        cups[0], cups[1] = cups[1], cups[0]
        #temp = cups[0]
        #cups[0] = cups[1]
        #cups[1] = temp
    elif move == "B":
        cups[1], cups[2] = cups[2], cups[1]
        #temp = cups[1]
        #cups[1] = cups[2]
        #cups[2] = temp
    else:
        cups[0], cups[2] = cups[2], cups[0]
        #temp = cups[0]
        #cups[0] = cups[2]
        #cups[2] = temp
    return cups

cups = [0, 0, 0]
cup, moves = [line.strip() for line in sys.stdin]

cups[int(cup) - 1] += 1

for move in moves:
    cupmove(move, cups)

print(cups.index(max(cups)) + 1)
