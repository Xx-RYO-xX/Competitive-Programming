import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from decimal import Decimal, getcontext
    getcontext().prec = 100
    a, b = map(Decimal, input().split())
    print(int(a*b))


if __name__ == '__main__':
    sys.exit(main())
