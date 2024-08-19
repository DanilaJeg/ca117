#!/usr/bin/env python3

import sys


digits = sys.stdin.readlines()
lim = int(digits[0].strip())
digits = digits[1:]
digits = digits[0].strip().split()

i = 0
while i < len(digits) and lim > 0:
    bucket = int(digits[i])
    lim -= bucket
    if lim < 0:
        i -= 1
    i += 1

print(i)
