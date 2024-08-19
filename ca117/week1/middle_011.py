#!/usr/bin/env python3

import sys

for word in sys.stdin:
    if len(word) % 2 == 0:
        print("No middle character!")
    else:
        print(len(word) // 2 + 1)
