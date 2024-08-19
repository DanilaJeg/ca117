#!/usr/bin/env python3

import sys

r = [int(x.strip()) for x in sys.stdin]

for num in r:
     print("Non-multiples of 3 replaced:", [0 if x % 3 else x for x in range(1, num + 1)])
