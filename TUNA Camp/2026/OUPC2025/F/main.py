import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    MOD = 998244353
    n = int(input())
    a = list(map(int, input().split()))

    if all([i == 1 for i in a]):
        ans = 1
        for i in range(1, n + 1):
            ans *= i % MOD
            ans %= MOD

        print(ans % MOD)
    if n == 1:
        print(1)


if __name__ == "__main__":
    main()
