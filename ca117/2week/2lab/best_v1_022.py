#!/usr/bin/env python3

import sys

scores = {}

try:
    with open(sys.argv[1], "r") as f:
            for line in f:
                score = int(line.strip()[:2])
                name = line.strip()[3:]
                if score in scores:
                    None
                elif name not in scores:
                    scores[score] = name

            highest = 0
            for student in scores:
                if student > highest:
                    highest = student
            print(f'Best student: {scores[highest]}')
            print(f'Best mark: {highest}')
except FileNotFoundError:
    print(f'The file {sys.argv[1]} could not be opened.')
except ValueError:
    print(f'Invalid mark {line.strip()[:2]} encountered. Exiting.')
