#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

def qnou(w):
    w = w.lower().replace("qu", "--")
    return 'q' in w

qnous = [w for w in words if qnou(w)]
print("Words with q but no u:", qnous)
