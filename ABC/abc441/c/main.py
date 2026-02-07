import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))


if __name__ == "__main__":
    main()
