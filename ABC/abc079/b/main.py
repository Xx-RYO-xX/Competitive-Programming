import sys 


def input():return sys.stdin.readline().rstrip()

from functools import cache

@cache
def ryuka(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return ryuka(n-1)+ryuka(n-2)


def main():
    n = int(input())
    print(ryuka(n))


if __name__ == '__main__':
    sys.exit(main())
