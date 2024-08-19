#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = sorted([int(x) for x in line.strip().split()], reverse=True)
    total = sum(nums) - sum(nums[2::3])
    print(total)
