#!/usr/bin/env python3

import sys

dic = {}

def doubleV(word):
    count = 0
    vowels = ["aa", "ee", "ii", "oo", "uu"]
    for v in vowels:
        count += word.count(v)
    return count

for word in sys.stdin:
    word = word.strip()
    if word not in dic:
        dic[word] = doubleV(word)

print(max(dic, key=dic.get))
