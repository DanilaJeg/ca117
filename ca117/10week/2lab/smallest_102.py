
#!/usr/bin/env python3

def smallest(ls):
    if len(ls) == 1:
        return ls[0]
    rest = smallest(ls[1:])
    return ls[0] if ls[0] < rest else rest

def main():
    print(smallest([6,5,1,3,4]))
    print(smallest([6,5,11,3,4]))
    print(smallest([6,15,11,14,14]))
    print(smallest([6,15,11,13,4]))

if __name__ == '__main__':
    main()
