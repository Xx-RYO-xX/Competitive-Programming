import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    print(a * 12 + b)


if __name__ == "__main__":
    main()
