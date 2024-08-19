#!/usr/bin/env python3

import sys

def checker(ch):
    if len(ch[0]) == len(ch[1]):
        return "safe"
    return "unsafe"

for line in sys.stdin:
    word = line.strip().strip("|")
    check = line.strip().split(word)
    print(checker(check))
