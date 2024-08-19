#!/usr/bin/env python3

import sys


for line in sys.stdin:
    numbers = [int(digit) for digit in line.strip().split() if line.strip().split().count(digit) == 1]
    print(max(numbers, default="none"))
