import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import bisect

    n = int(input())
    a = sorted(map(int, input().split()))

    ans = 0
    for A in a:
        ans += bisect.bisect_left(a, A) * (n - bisect.bisect_right(a, A))

    print(ans)


if __name__ == "__main__":
    main()
