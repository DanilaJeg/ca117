#!/usr/bin/env python3

import sys
import string

wordsD = {}

punc = '''!()-[]{};:"\,<>./?@#$%^&*_~'''

lines = [line.strip().lower() for line in sys.stdin]


for line in lines:
    line = line.translate(str.maketrans("", "", punc))
    line = line.split()

    words = [word.lower() for word in line]
    
    for word in words:
        if word not in wordsD:
            wordsD[word] = 0
        wordsD[word] += 1


for word in sorted(wordsD):
    print(word, ":", wordsD[word])
