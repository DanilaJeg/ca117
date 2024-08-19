#!/usr/bin/env python3

import sys


lines = sys.stdin.readlines()
maximum = int(lines[0].strip())
lines.remove(lines[0])

denied = 0
total = 0
for line in lines:
    status, num = line.strip().split()
    if status == "enter":
        if total + int(num) > maximum:
            denied += 1
        else:
            total += int(num)
    else:
        total -= int(num)

print(denied)
