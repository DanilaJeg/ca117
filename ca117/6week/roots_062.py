#!/usr/bin/env python3

import sys

def roots(a, b, c):
    root1 = ((-1 * b) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    root2 = ((-1 * b) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    roots = sorted([round(root1, 1), round(root2, 1)])
    return roots


for line in sys.stdin:
    a, b, c = line.strip().split()
    try:
        print(*roots(int(a), int(b), int(c)), sep = ", ")
    except:
        print(None)

