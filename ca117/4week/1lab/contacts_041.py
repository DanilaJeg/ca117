#!/usr/bin/env python3

import sys

phonebook = {}

with open(sys.argv[1], "r") as f:
    f = f.readlines()
    for line in f:
        name, phone = line.strip().split()
        if name not in phonebook:
            phonebook[name] = phone

names = [name.strip() for name in sys.stdin]

for name in names:
    print("Name:", name)
    try:
        print("Phone:", phonebook[name])
    except KeyError:
        print("No such contact")
