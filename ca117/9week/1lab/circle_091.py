#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def __str__(self):
        return f'({self.x:03.1f}, {self.y:03.1f})'
    
class Circle(object):
    
    def __init__(self, centre=None, rad=1):
        if centre == None:
            self.centre = Point()
        else:
            self.centre = centre
        self.radius = rad

    def __str__(self):
        return f'Centre: ({self.centre.x:.1f}, {self.centre.y:.1f})\nRadius: {self.radius}'


def main():
    p1 = Point(2, 3)
    c1 = Circle(p1, 5)

    assert(c1.centre is p1)
    assert(c1.radius == 5)

    c2 = Circle()
    assert(isinstance(c2.centre, Point))
    assert(c2.radius == 1)

    c3 = Circle()
    assert(c3.centre is not c2.centre)

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()
