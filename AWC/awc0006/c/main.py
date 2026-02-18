import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import ceil

    n, m, d = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 0
    for T in t:
        if T <= m:
            continue
        ans += ceil((T - m) / d)
    print(ans)


if __name__ == "__main__":
    main()
