#!/usr/bin/env python3


class MP3Track(object):

    def __init__(self, title, sec, artist=None):
        self.title = title
        self.duration = sec
        if artist == None:
            artist = []
        self.artist = artist

    def __str__(self):
        return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {self.duration}'

class MP3Collection(object):

    def __init__(self):
        self.tracks = {}

    def add(self, t):
        self.tracks[t.title] = t

    def remove(self, title):
        if title in self.tracks:
            del self.tracks[title]

    def lookup(self, title):
        if title in self.tracks:
            return self.tracks[title]
        return None

    def __add__(self, other):
        new = MP3Collection()
        for track in self.tracks:
            new.add(track)
        for track in other.tracks:
            new.add(track)
        return new


def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c1 = MP3Collection()
    c1.add(t1)
    c1.add(t2)

    c2 = MP3Collection()
    c2.add(t3)

    # Make a new collection from two existing ones
    c3 = c1 + c2
    assert(isinstance(c3, MP3Collection))
    assert(c3 is not c1)
    assert(c3 is not c2)

if __name__ == '__main__':
    main()
