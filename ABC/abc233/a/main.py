import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from decimal import Decimal
    from math import ceil
    x, y = map(int, input().split())

    ans = ceil((y-x)/10)
    print(ans if ans > 0 else 0)


if __name__ == '__main__':
    sys.exit(main())
