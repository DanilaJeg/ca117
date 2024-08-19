#!/usr/bin/env python3

import sys

nums = [int(n) for n in input().split()]
temps = list()

for i in range(len(nums) - 2):
    temps.append(max(nums[i], nums[i + 2]))

print(f'{temps.index(min(temps)) + 1} {min(temps)}')
