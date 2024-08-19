#!/usr/bin/env python3

import sys
from math import pi

for n in sys.stdin:
    n = int(n.strip())
    print(f'{pi:.{n}f}')
