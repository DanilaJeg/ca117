#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

longest = 0
for line in lines:
    line = line.strip()
    if len(line) > longest:
        longest = len(line)

for line in lines:
    line = line.strip()
    print(f'{line:^{longest}}')
