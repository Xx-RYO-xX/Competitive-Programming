import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import gcd

    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
