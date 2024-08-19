#!/usr/bin/env python3

import sys

countries = [country.strip() for country in sys.stdin][1:]
search, count = countries[-1].split()

wanted = []

for c in countries:
    country, year = c.split()
    if country == search:
        wanted.append(int(year))

print(sorted(wanted)[int(count)])
