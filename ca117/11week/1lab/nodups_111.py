#!/usr/bin/env python3

import sys

words = set()
lines = []
for line in sys.stdin:
    line = line.strip().split()
    new = ""
    for word in line:
        wordToCheck = None
        if word[-1] not in "abcdefghijklmnopqrstuvwxyz":
            wordToCheck = word[:-1]
        else:
            wordToCheck = word

        if wordToCheck.lower() in words:
            new += ". "
        else:
            words.add(wordToCheck.lower())
            new += word + " "
    lines.append(new.rstrip())

print("\n".join(lines))
