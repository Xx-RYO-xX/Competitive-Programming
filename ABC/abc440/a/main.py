import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y = map(int, input().split())

    print(x * 2**y)


if __name__ == "__main__":
    main()
