#!/usr/bin/env python3

import sys

endings = {
    "ch": ["", "es"],
    "sh": ["", "es"],
    "x": ["", "es"],
    "s": ["", "es"],
    "z": ["", "es"],
    
    "f": ["f", "ves"],
    "fe": ["fe", "ves"],
    
    "o": ["", "es"],
}

for word in sys.stdin:
    word = word.strip()

    endinFound = False
    for ending in endings.items():
        if word.endswith(ending[0]):
            endinFound = True
            word = word[:len(word) - len(ending[1][0])]
            word += ending[1][1]
            print(word)
            break

    if endinFound == False:
        if word[-2] not in "aeiou" and word[-1] == "y":
            word = word[:-1] + "ies"
            print(word)
        else:
            word += "s"
            print(word)
