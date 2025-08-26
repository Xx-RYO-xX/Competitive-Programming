import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y = map(int, input().split())
    print((x + y - 1) % 12 + 1)


if __name__ == "__main__":
    main()
