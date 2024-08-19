#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, sec):
        self.title = title
        self.duration = sec

    def __str__(self):
        return f'Title: {self.title}\nDuration: {self.duration}'

class MP3Collection(object):

    def __init__(self):
        self.tracks = {}

    def add(self, t):
        self.tracks[t.title] = t

    def remove(self, title):
        if title in self.tracks:
            del self.tracks[title]

    def lookup(self, title):
        if title not in self.tracks:
            return None
        return self.tracks[title]


def main():
    t1 = MP3Track('Fools Gold', 604)
    t2 = MP3Track('Shallow', 197)
    t3 = MP3Track('Telephone', 220)

    c = MP3Collection()
    
    c.add(t1)
    c.add(t2)
    c.add(t3)

    t = c.lookup('Fools Gold')
    assert(isinstance(t, MP3Track))
    assert(t.title == 'Fools Gold')
    assert(t.duration == 604)

    c.remove('Fools Gold')
    t = c.lookup('Fools Gold')
    assert(t is None)

if __name__ == '__main__':
    main()
