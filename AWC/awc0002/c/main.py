import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import math

    n, m = map(int, input().split())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans = max(ans, math.ceil((m - a) / b))

    print(ans)


if __name__ == "__main__":
    main()
