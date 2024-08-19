#!/usr/bin/env python3

import sys

for email in sys.stdin:
    email = email.split("@")
    email = email[0].split(".")
    fname = email[0].capitalize()
    sname = email[1]
    i = 0
    while i < len(sname) and sname[i] >= "a" and sname[i] <= "z":
        i += 1
    print(fname + " " + sname[:i].capitalize())
