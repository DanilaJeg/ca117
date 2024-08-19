#!/usr/bin/env python3

# 1, 1 , 2 , 3 , 5, 8, 13, 21, 34 ...

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)rpn_101.py
