import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import gcd

    n = int(input())
    a = list(map(int, input().split()))

    print(gcd(*a))


if __name__ == "__main__":
    main()
