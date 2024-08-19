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
    "c": num[2],
    "d": num[3],
    "e": num[4],
    "f": num[5]
}
string = ""
for i in order:
    string += str(variable[i]) + " " 
print(string.strip())
