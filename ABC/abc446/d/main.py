import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n = int(input())
    a = list(map(int, input().split()))

    dp = defaultdict(int)

    for A in a:
        dp[A] = dp[A - 1] + 1

    print(max(dp.values()))


if __name__ == "__main__":
    main()
