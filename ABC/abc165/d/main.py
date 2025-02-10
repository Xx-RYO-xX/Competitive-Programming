import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from decimal import Decimal, getcontext
    from math import floor
    getcontext().prec = 100
    a, b, n = map(Decimal, input().split())
    def calc(x):
        return floor(a*x/b) - a*floor(x/b)

    ans = max(0, calc(n))
    if b-1 <= n:
        ans = max(ans, calc(b-1))
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
