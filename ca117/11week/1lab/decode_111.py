#!/usr/bin/env python3

import sys

def decode(s):
    vowels = {"a", "e", "i", "o", "u"}
    i = 0
    while i < len(s):
        if s[i] in vowels:
            s = s[:i + 1] + s[i + 3:]
        i += 1
    return s

for line in sys.stdin:
    line = line.strip()
    print(decode(line))
