#!/usr/bin/env python3

import sys

def punct(string):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    for char in string:
        if char not in chars:
            string = string.replace(char, "", 1)
    return string

def palindrome(string):
    if string == string[::-1]:
        return True
    return False

for word in sys.stdin:
    word = punct(word.strip().lower())
    print(palindrome(word))
