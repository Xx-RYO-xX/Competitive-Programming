import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        n = int(input())
        for __ in range(n - 1):
            a, b = map(int, input().split())


if __name__ == "__main__":
    main()
