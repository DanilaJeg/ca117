#!/usr/bin/env python3

import sys

nums = sys.stdin.readline().strip().split()

towers = 1
i = 0
while i + 1 < len(nums):
    curr = int(nums[i + 1])
    prev = int(nums[i])
    if curr > prev:
        towers += 1
    i += 1

print(towers)
