#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, ID, mod=None):
        self.name = name
        self.sid = ID
        if mod == None:
            self.mod = []
        else:
            self.mod = sorted(mod)

    def average_mark(self):
        total = 0
        for _, mark in self.mod:
            total += mark
        return total / len(self.mod)

    def __str__(self):
        return f'Name: {self.name}\nID: {self.sid}\nModules: {", ".join(module for module, _ in self.mod)}\nAverage mark: {self.average_mark():.0f}'
