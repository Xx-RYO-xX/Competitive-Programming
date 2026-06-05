import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import ceil

    n = int(input())
    a = list(list(map(int, input().split())))

    n -= a.count(0)
    a = sum(a)

    print(ceil(a / n))


if __name__ == "__main__":
    main()
