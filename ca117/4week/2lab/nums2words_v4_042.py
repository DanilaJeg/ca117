#!/usr/bin/env python3

import sys

converted = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred"
}

for line in sys.stdin:
    numbers = [int(n) for n in line.strip().split()]
    conv = []
    for n in numbers:
        if n >= 20:
            ten = (n // 10) * 10
            if n % 10 != 0:
                dig = n % 10
                num = [converted[ten], converted[dig]]
            else:
                num = [converted[ten]]
            conv.append("-".join(num))
        else:
            conv.append(converted[n])
    print(" ".join(conv))
