#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline().strip())
jumps = sys.stdin.readline().strip().split()
jump1 = int(jumps[0])
jump2 = int(jumps[1])

def jumps(n, j1, j2):
    # base cases
    if n == 0:
        return 1
    if n < 0:
        return 0

    m = n - j1
    o = n - j2

    return jumps(m, j1, j2) + jumps(o, j1, j2)



print(jumps(n, jump1, jump2))

