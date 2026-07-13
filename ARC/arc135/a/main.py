def main():
    import sys
    from math import floor, ceil
    from functools import cache

    input = sys.stdin.readline

    x = int(input())
    MOD = 998244353

    sys.setrecursionlimit(10**9)

    @cache
    def f(xx):
        if xx <= 3:
            return xx
        return f(xx // 2) * f(-(-xx // 2)) % MOD

    print(f(x) % MOD)


if __name__ == "__main__":
    main()
