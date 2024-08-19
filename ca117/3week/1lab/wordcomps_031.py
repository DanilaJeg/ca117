#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

def acount(w):
    acount = 0
    for c in w:
        if c == "a" or c == "A":
            acount += 1
    return acount

def qcount(w):
    qcount = 0
    for c in w:
        if c == "q" or c == "Q":
            qcount += 1
    return qcount

def ending(w):
    if "cie" in w:
        return True
    return False

print("Words containing 17 letters:", [w for w in words if len(w) == 17])
print("Words containing 18+ letters:", [w for w in words if len(w) >= 18])
print("Words with 4 a's:", [w for w in words if acount(w) == 4])
print("Words with 2+ q's:", [w for w in words if qcount(w) >= 2])
print("Words containing cie:", [w for w in words if ending(w)])
print("Anagrams of angle:", [w for w in words if sorted("angle") == sorted(w.lower()) and w != "angle"])
