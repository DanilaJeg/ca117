#!/usr/bin/env python3

import sys

def punct(string):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    for char in string:
        if char not in chars:
            string = string.replace(char, "", 1)
    return string

inp = sys.stdin.read().split()
words = []

i = 0
for word in inp:
    inp[i] = punct(word.lower())
    i += 1

for word in inp:
    if word not in words:
        words.append(word)
print(len(words) - 1)
