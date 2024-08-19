#!/usr/bin/env python3

import sys

endings = {
    "ch": [None,"es"], 
    "sh": [None, "es"],
    "x": [None, "es"],
    "s": [None, "es"],
    "z": [None, "es"],

    "f": ["f", "ves"],
    "fe": ["fe", "ves"],

    "o": ["o", "es"],
}


for line in sys.stdin:
    word = line.strip()
    if word.endswith("ch")
