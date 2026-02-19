import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, t, k = map(int, input().split())
    h = list(map(int, input().split()))

    d = min(h) - 1
    ans = 0
    for hh in h:
        if hh - d <= t + k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
