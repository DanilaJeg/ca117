#!/usr/bin/env python3

class Stack(object):
    
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.stack)

def main():

    s = Stack()

    print(len(s))
    s.push(1)
    print(s.top())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())
    try:
        print(s.pop())
    except IndexError:
        print('Error')
    try:
        print(s.top())
    except IndexError:
        print('Error')
    s.push(1)
    s.push(2)
    s.push(3)
    print(len(s))
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())

if __name__ == '__main__':
    main()
