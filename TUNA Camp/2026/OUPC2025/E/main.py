import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    MOD = 998244353
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(1, m + 1):
        if i != a[0]:
            for j in range(1, m + 1):
                if j != a[1]:
                    ans += (i + j) % m

    print(ans % MOD)


if __name__ == "__main__":
    main()
