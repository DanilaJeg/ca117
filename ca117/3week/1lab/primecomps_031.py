#!/usr/bin/env python3

import sys

r = [int(num.strip()) for num in sys.stdin]

for num in r:
    print("Primes:", [x for x in range(2, num) if (x == 2 or x == 3 or x == 5 or x == 7) or not(x % 2 == 0) and not(x % 3 == 0) and not(x % 5 == 0) and not(x % 7 == 0)])
