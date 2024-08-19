#!/usr/bin/env python3

import sys

lines = [word.strip() for word in sys.stdin]
nums = [int(x) for x in lines if x.isdigit()]
n = nums[-1]
nums.remove(n)
guesses = [x for x in lines if not(x.isdigit())]
guesses.remove("correct")
actual = []
for x in nums:
    if x > n:
        actual.append("lower")
    else:
        actual.append("higher")

if actual == guesses:
    print("Bert can be trusted")
else:
    print("Bert is not to be trusted")
