#!/usr/bin/env python3

import sys

conversion = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}

def convert(nums):
    conv = []
    for n in range(len(nums)):
        conv.append(conversion[nums[n]])
    return conv



for line in sys.stdin:
    nums = line.strip().split()
    convert(nums)
    print(" ".join(convert(nums)))
