#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, sec):
        self.title = title
        self.duration = sec

    def __str__(self):
        return f'Title: {self.title}\nDuration: {self.duration}'
