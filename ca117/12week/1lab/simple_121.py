#!/usr/bin/env python3

import sys
'''
for line in sys.stdin:
    string = line.strip()
    letters = set(string)
    ls = []
    for c in letters:
        t = (c, string.count(c))
        ls.append(t)
    ls = sorted(ls, key = lambda x: x[1])
    distinct = 0
    i = 0
    while len(letters) > 2:
        letters.remove(ls[i][0])
        distinct += ls[i][1]
        i += 1
    print(distinct) '''

for line in sys.stdin:
    letters = {}
    for c in line.strip():
        if c not in letters:
            letters[c] = 0
        letters[c] += 1
    print(sum(sorted(letters.values(), reverse=True)[2:]))
