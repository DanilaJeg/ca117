#!/usr/bin/env python3

import sys

for i in sys.stdin:
    word = i.strip()
    word = word.capitalize()
    last = word[-1]
    word = word[:-1]
    last = last.capitalize()
    word += last
    print(word)
