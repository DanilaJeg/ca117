#!/usr/bin/env python3

import sys


r = [int(x.strip()) for x in sys.stdin]

for num in r:
    list1 = [x for x in range(1, num + 1) if not(x % 3)]
    list2 = [x*x for x in range(1, num + 1) if not(x % 3)]
    list3 = [x*2 for x in range(1, num + 1) if not(x % 4)]
    list4 = [x for x in range(1, num + 1) if not(x % 4) or not(x % 3)]
    list5 = [x for x in range(1, num + 1) if not(x % 4) and not(x % 3)]
    print("Multiples of 3:", list1)
    print("Multiples of 3 squared:", list2)
    print("Multiples of 4 doubled:", list3)
    print("Multiples of 3 or 4:", list4)
    print("Multiples of 3 and 4:", list5)
