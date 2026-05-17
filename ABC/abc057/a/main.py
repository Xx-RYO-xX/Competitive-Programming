import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    print((a + b) % 24)


if __name__ == "__main__":
    main()
