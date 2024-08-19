#!/usr/bin/env python3

import sys

nums, order = sys.stdin.readlines()
num = nums.strip().split()
order = list(order.strip().lower())

for n in range(len(num)):
    num[n] = int(num[n])

num = sorted(num)

variable = {
    "a": num[0],
    "b": num[1],
    "c": num[2]
}

print(variable[order[0]], variable[order[1]], variable[order[2]])

string = ""
for i in order:
    string += str(variable[i]) + " "

print(string.strip())
