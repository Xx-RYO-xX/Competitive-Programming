import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    open_start = 0

    for A in a:
        if A >= open_start:
            ans += A - open_start
            open_start = A + 100

    if open_start < t:
        ans += t - open_start

    print(ans)


if __name__ == "__main__":
    main()
