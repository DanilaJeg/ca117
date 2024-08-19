#!/usr/bin/env python3

import sys
# both x and y have to be positive to be in quadrant 1:

quads = {
    (True, True): 1,
    (True, False): 2,
    (False, False): 3,
    (False, True): 4
}

for nums in sys.stdin:
    line = nums.strip().split()
    x = int(line[0])
    y = int(line[1])
    print(quads[(x > 0, y > 0)])
