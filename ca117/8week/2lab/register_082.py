#!/usr/bin/env python3

class CashRegister(object):
    
    def __init__(self, total=0, count=0):
        self.total = total
        self.count = count

    def add_item(self, price):
        self.total += price
        self.count += 1

    def clear(self):
        self.total = 0
        self.count = 0

    def __str__(self):
        return f'Items: {self.count}\nTotal: {self.total:.2f}'



import sys

def main():

    cr = CashRegister()
    print(cr)

    cr.add_item(3.28)
    assert(cr.total == 3.28)
    assert(cr.count == 1)

    cr.add_item(12.92)
    print(cr)

    cr.clear()

    cr.add_item(9.1)
    print(cr)

if __name__ == '__main__':
    main()
