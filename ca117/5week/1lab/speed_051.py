#!/usr/bin/env python3

import sys

r = [line.strip() for line in sys.stdin]

speeds = []
line = r[0]
pt, pd = [int(t) for t in line.strip().split()]

for line in r[1:]:
    ct, cd = [int(t) for t in line.strip().split()]
    speed = (cd - pd) // (ct - pt)
    speeds.append(speed)
    pt, pd = ct, cd

print(max(speeds))

