def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline
    n = int(input())
    a = [0] + list(map(int, input().split()))

    MOD = 998244353
    bunsuu = [0]
    for i in range(1, n + 1):
        bunsuu.append((bunsuu[-1] + pow(i, MOD - 2, MOD)) % MOD)

    a = list(accumulate(a))

    # print(a)
    # print(bunsuu)

    ans = 0
    for i in range(1, n + 1):
        bun = (bunsuu[i] - bunsuu[0]) - (bunsuu[n - i] - bunsuu[0])
        ans = (ans + bun * a[i]) % MOD

    print(ans % MOD)


if __name__ == "__main__":
    main()
