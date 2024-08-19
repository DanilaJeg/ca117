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

    def __eq__(self, other):
        return self.total_time() == other.total_time()

    def __lt__(self, other):
        return self.total_time() < other.total_time()
 
    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.total_time()}'

class Triathlon(object):
    
    def __init__(self):
        self.athletes = {}

    def add(self, t):
        self.athletes[t.tid] = t
        
    def lookup(self, search):
        return lookup[search]

    def remove(self, tid):
        del self.athletes[self.lookup(tid)]

    def best(self):
        print(self.athletes.values())
        return min(self.athletes.values())

    def worst(self):
        return max(self.athletes.values())

    def __str__(self):
        output = []
        for athlete in self.athletes:
            output.append(f'Name: {athlete.name}\nID: {athlete.tid}')
        return "\n".join(sorted(output))


def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
