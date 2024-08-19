#!/usr/bin/env python3

import sys

scores = {}

try:
    with open(sys.argv[1], "r") as f:

        for line in f:
            try:
                line = line.split()
                score, name = int(line[0]), " ".join(line[1:])
                if score not in scores:
                    scores[score] = []
                    scores[score].append(name)
                else:
                    scores[score].append(name)
                

            except ValueError:
                print(f'Invalid mark {line.strip()[:2]} encountered. Skipping.')

        highest = 0
        for student in scores:
            if student > highest:
                highest = student
        print(f'Best student(s): {", ".join(scores[highest])}')
        print(f'Best mark: {highest}')
except FileNotFoundError:
    print(f'The file {sys.argv[1]} could not be opened.')


