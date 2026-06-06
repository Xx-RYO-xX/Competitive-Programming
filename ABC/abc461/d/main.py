import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w, k = map(int, input().split())
    s = [None] * (h)
    for i in range(h):
        s[i] = list(map(int, input()))
    accm_s = [[0] * (w + 1) for i in range(h + 1)]

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            accm_s[i][j] = accm_s[i][j - 1] + s[i - 1][j - 1]

    for j in range(1, w + 1):
        for i in range(1, h + 1):
            accm_s[i][j] = accm_s[i - 1][j] + accm_s[i][j]

    cnt = dict()
    ans = 0
    for r1 in range(1, h + 1):
        for r2 in range(r1, h + 1):
            cnt.clear()
            cnt[0] = 1
            for c2 in range(1, w + 1):
                now_sum = accm_s[r2][c2] - accm_s[r1 - 1][c2]
                ans += cnt.get(now_sum - k, 0)
                cnt[now_sum] = cnt.get(now_sum, 0) + 1

    print(ans)


if __name__ == "__main__":
    main()
