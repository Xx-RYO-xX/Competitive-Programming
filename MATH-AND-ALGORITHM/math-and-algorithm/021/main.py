import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import comb

    n, r = map(int, input().split())
    print(comb(n, r))


if __name__ == "__main__":
    main()
