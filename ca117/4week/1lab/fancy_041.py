#!/usr/bin/env python3

import sys

phonebook = {}

with open(sys.argv[1], "r") as f:
    f = f.readlines()
    for line in f:
        name, phone, mail = line.strip().split()
        if name not in phonebook:
            phonebook[name] = [phone, mail]

names = [name.strip() for name in sys.stdin]
print(phonebook)

for name in names:
    print("Name:", name)
    try:
        print("Phone:", phonebook[name][0])
        print("Email:", phonebook[name][1])
    except KeyError:
        print("No such contact")
