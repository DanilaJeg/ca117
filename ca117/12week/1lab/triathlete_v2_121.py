#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.event = {}

    def add_time(self, event, time):
        self.event[event] = time

    def get_time(self, event):
        return self.event[event]

    def total_time(self):
        return sum(self.event.values())

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.total_time()}'

