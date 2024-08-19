#!/usr/bin/env python3


def sumup(x):
    if x == 0:
        return 0
    return x + sumup(x - 1)

def main():
    print(sumup(0))
    print(sumup(1))
    print(sumup(12))

if __name__ == '__main__':
    main()
