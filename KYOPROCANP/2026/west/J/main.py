## https://tjkendev.github.io/procon-library/python/dp/lcs.html


def solve(S, T):
    L1 = len(S)
    L2 = len(T)
    dp = [[0] * (L2 + 1) for i in range(L1 + 1)]

    for i in range(L1 - 1, -1, -1):
        for j in range(L2 - 1, -1, -1):
            r = max(dp[i + 1][j], dp[i][j + 1])
            if S[i] == T[j]:
                r = max(r, dp[i + 1][j + 1] + 1)
            dp[i][j] = r
    return dp[0][0]


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    s = input()[:-1]
    for _ in range(q):
        t = input()[:-1]
        print(solve(s, t))


if __name__ == "__main__":
    main()
