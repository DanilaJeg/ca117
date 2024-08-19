#!/usr/bin/env python3

import sys

def lessthan(number):
    number = str(number)
    d = [int(digit) for digit in number if int(digit) > 0]
    total = 1
    for num in range(len(d)):
        total *= d[num]
    if total < 10:
        return total
    return lessthan(total)

for line in sys.stdin:
    num = line.strip()
    print(lessthan(num))
