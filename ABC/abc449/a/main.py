import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import pi

    d = int(input())
    print((d / 2) ** 2 * pi)


if __name__ == "__main__":
    main()
