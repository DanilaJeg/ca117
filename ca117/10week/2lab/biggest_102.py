#!/usr/bin/env python3

def biggest(ls, big=None):
    if len(ls) == 0:
        return big
    elif big == None or ls[0] > big:
        big = ls[0]
    return biggest(ls[1:], big)
