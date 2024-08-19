#!/usr/bin/env python3

import sys

for i in sys.stdin:
    word = i.strip()
    if len(word) > 2:
        print(word[1:-1])
