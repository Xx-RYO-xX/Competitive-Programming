import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from math import sqrt
    from decimal import Decimal, getcontext
    
    getcontext().prec = 4000

    a, b, c = map(Decimal, input().split())
    
    if a.sqrt() + b.sqrt() < c.sqrt():
        print("Yes")
    else:
        print("No")
        


if __name__ == '__main__':
    main()
