#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point):
        return (((point.x - self.x) ** 2) + ((point.y - self.y) ** 2)) ** 0.5

    def __str__(self):
        return f'({self.x:.1f}, {self.y:.1f})'




def main():
    p1 = Point()

    print(p1)

    p2 = Point(3, 4)

    assert(p2.x == 3)
    assert(p2.y == 4)
    print(p2)

    print(p1.distance(p2))

if __name__ == '__main__':
    main()
