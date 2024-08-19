#!/usr/bin/env python3

def swap_keys_values(d):
    reverse = {}
    for key in d:
        if d[key] not in reverse:
            reverse[d[key]] = key
    return reverse
