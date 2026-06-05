import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, k = map(int, input().split())

    left = 0
    right = 2 * k
    while left < right:
        mid = (left + right) // 2


if __name__ == "__main__":
    main()
