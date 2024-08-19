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

    def sort_key(self):
        return self.average_mark()

class Classlist(object):

    def __init__(self, cl=None):
        if cl == None:
            self.cl = []
        else:
            self.cl = []

    def add(self, student):
        self.cl.append(student)
        self.cl.sort(key=Student.sort_key, reverse = True)

    def __str__(self):
        schedule_str = "\n".join(str(student) for student in self.cl)
        return schedule_str

        

def main():

    cl = Classlist()

    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    cl.add(s1)
    cl.add(s2)

    print(cl)


if __name__ == '__main__':
    main()
