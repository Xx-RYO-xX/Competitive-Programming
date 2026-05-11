import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import ceil

    n = int(input())
    print(ceil(n / 2))


if __name__ == "__main__":
    main()
