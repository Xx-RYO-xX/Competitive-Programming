import sys 


def input():return sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**9)
from functools import cache
@cache
def f(x):
    if x < 2:
        return 0
    return x+f((x+1)//2)+f((x//2))


def main():
    n = int(input())
    print(f(x=n))


if __name__ == '__main__':
    sys.exit(main())
