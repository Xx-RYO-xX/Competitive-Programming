import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, m = map(int, input().split())
    st = list(map(int, input().split()))
    s, t = min(st), max(st)
    ans = 0
    for _ in range(m):
        p, v = map(int, input().split())
        if s <= p <= t:
            ans += v

    print(ans)


if __name__ == "__main__":
    main()
