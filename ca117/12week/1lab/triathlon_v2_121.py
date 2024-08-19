#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}'

class Triathlon(object):
    
    def __init__(self):
        self.athletes = {}

    def add(self, t):
        self.athletes[t] = t.tid
        
    def lookup(self, search):
        for key in self.athletes:
            if self.athletes[key] == search:
                return key

    def remove(self, tid):
        del self.athletes[self.lookup(tid)]

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

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
