#!/usr/ben/env pytho3


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
            self.centre = Point(0, 0)
        else:
            self.centre = centre
        self.radius = rad

    def __add__(self, other):
        return Circle(self.centre.midpoint(other.centre), self.radius + other.radius)

    def __str__(self):
        return f'Centre: ({self.centre.x:.1f}, {self.centre.y:.1f})\nRadius: {self.radius}'



def main():
    p1 = Point()
    p2 = Point(4, 6)

    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)

    c3 = c1 + c2
    assert(isinstance(c3, Circle))
    print(c3)

if __name__ == '__main__':
    main()
