#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    f = f.readlines()
    translated = []
    for line in f:
        translated.append(line.strip().split()[1])


conversion = {
    "0": translated[0],
    "1": translated[1],
    "2": translated[2],
    "3": translated[3],
    "4": translated[4],
    "5": translated[5],
    "6": translated[6],
    "7": translated[7],
    "8": translated[8],
    "9": translated[9],
    "10": translated[10]
}

def convert(nums):
    conv = []
    for n in range(len(nums)):
        if nums[n] in conversion:
            conv.append(conversion[nums[n]])
        else:
            conv.append("unknown")
    return conv



for line in sys.stdin:
    nums = line.strip().split()
    convert(nums)
    print(" ".join(convert(nums)))
