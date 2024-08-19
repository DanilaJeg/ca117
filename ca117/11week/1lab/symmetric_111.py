#!/usr/bin/env python3

import sys

l = [word.strip() for word in sys.stdin]
l2 = []

lenToString = {}
for word in l:
    if len(word) not in lenToString:
        lenToString[len(word)] = []
        lenToString[len(word)].append(word)
    else:
        lenToString[len(word)].append(word)

lengths = [len(s) for s in l]

for n in lengths:
    if lengths.count(n) == 2:
        l2.append(n)
        lengths.remove(n)

l2.sort(reverse = True)
lengths = lengths + l2

strings = []
for l in lengths:
    if lenToString[l]:
        strings.append(lenToString[l].pop(0))

print("\n".join(strings))
