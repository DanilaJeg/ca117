#!/usr/bin/env python3

def reverse(ls):
    if ls == []:
        return []
    return [ls[-1]] + reverse(ls[:-1])
