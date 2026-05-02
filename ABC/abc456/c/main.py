import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()

    MOD = 998244353
    ans = 0
    cnt = 1

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            ans %= MOD
            cnt = 1

    ans += cnt * (cnt + 1) // 2
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
