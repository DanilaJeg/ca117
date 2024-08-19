#!/usr/bin/env python3

import sys

def matcher(brackets):
    stack = []
    closeToOpen = {"}": "{", "]": "[", ")": "("}

    for b in brackets:
        if b in closeToOpen:
            if stack and stack[-1] == closeToOpen[b]:
                stack.pop()
            else:
                return False
        else:
            stack.append(b)
    return not stack

string = "print)'hello')"
b = "(){}[]"

for char in string:
    if char not in b:
        brackets = string.replace(char, "")

print(matcher(brackets))
