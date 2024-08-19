#!/usr/bin/env python3

import sys

def lowercase(p):
    for char in p:
        if char >= "a" and char <= "z":
            return 1
    return 0

def uppercase(p):
    for char in p:
        if char >= "A" and char <= "Z":
            return 1
    return 0

def digit(p):
    for char in p:
        if char >= "0" and char <= "9":
            return 1
    return 0

def special(p):
    for char in p:
        if lowercase(char) + uppercase(char) + digit(char) == 0:
            return 1
    return 0

for line in sys.stdin:
    pwd = line.strip()
    print(lowercase(pwd) + uppercase(pwd) + digit(pwd) + special(pwd))

