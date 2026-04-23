import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    l, r = map(int, input().split())
    print(r + 1 - l)


if __name__ == "__main__":
    main()
