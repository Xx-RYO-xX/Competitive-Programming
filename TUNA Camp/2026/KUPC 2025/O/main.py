import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input()) + 1

    MOD = 998244353
    print(
        (pow(4, n - 1, MOD) - 3 * pow(3, n - 1, MOD) + 3 * pow(2, n - 1, MOD) - 1) % MOD
    )


if __name__ == "__main__":
    main()
