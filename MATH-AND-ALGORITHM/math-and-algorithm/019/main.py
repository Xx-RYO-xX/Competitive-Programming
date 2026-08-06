import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import comb

    n = int(input())
    a = list(map(int, input().split()))

    print(comb(a.count(1), 2) + comb(a.count(2), 2) + comb(a.count(3), 2))


if __name__ == "__main__":
    main()
