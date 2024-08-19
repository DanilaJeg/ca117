#!/usr/bin/env python3

def calculator(line):
    line = line.split()
    stack = []
    for c in line:
        if c.replace(".", "").isnumeric():
            stack.append(float(c))
        elif c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            n1, n2 = stack.pop(), stack.pop()
            stack.append(n2 - n1)
        elif c == "/":
            n1, n2 = stack.pop(), stack.pop()
            stack.append(n2 / n1)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "r":
            stack.append(stack.pop() ** 0.5)
        elif c == "n":
            stack.append(stack.pop() * -1)
    return stack.pop()
