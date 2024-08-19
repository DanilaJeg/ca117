#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, d):
        self.hour = hour
        self.minute = minute
        self.duration = d

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02} ({self.duration} minutes)'

    def sort_key(self):
        return self.hour, self.minute

class Schedule():

    def __init__(self):
        self.meetings = []

    def add(self, other):
        self.meetings.append(other)
        self.meetings.sort(key=Meeting.sort_key)

    def __str__(self):
        schedule_str = "Schedule\n--------\n" + "\n".join(str(meeting) for meeting in self.meetings)
        schedule_str += f"\nMeetings today: {len(self.meetings)}"
        return schedule_str
