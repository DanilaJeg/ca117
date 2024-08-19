#!/usr/bin/env python3

import sys

def product_of_digits(number):
    product = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            product *= digit
        number //= 10
    return product

for line in sys.stdin:
    num = int(line.strip())
    while num >= 10:
        num = product_of_digits(num)
    print(num)
