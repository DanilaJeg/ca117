#!/usr/bin/env python3

import sys

alph = "abcdefghijklmnopqrstuvwxyz"

for line in sys.stdin:
    missing = []
    line = line.strip().lower()
    for c in alph:
        if c not in line:
            missing.append(c)
    missing = "".join(missing)
    print("missing " +  missing if missing else "pangram")
    
