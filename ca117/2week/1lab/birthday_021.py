#!/usr/bin/env python3

import sys
import calendar

days = {
    0: "You were born on a Monday and Monday's child is fair of face.",
    1: "You were born on a Tuesday and Tuesday's child is full of grace.",
    2: "You were born on a Wednesday and Wednesday's child is full of woe.",
    3: "You were born on a Thursday and Thursday's child has far to go.",
    4: "You were born on a Friday and Friday's child is loving and giving.", 
    5: "You were born on a Saturday and Saturday's child works hard for a living.",
    6: "You were born on a Sunday and Sunday's child is fair and wise and good in every way."
}

for date in sys.stdin:
    day, month, year = date.strip().split()
    print(days[calendar.weekday(int(year), int(month), int(day))])
