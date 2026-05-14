import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import ceil

    n, x, t = map(int, input().split())
    print(t * ceil(n / x))


if __name__ == "__main__":
    main()
