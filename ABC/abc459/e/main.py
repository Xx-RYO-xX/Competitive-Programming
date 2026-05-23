import sys


def input():
    return sys.stdin.readline().rstrip()


## https://qiita.com/yggnoki/items/9be88106bcee8dde5739
class Comb:

    def __init__(self, maxn, mod):
        self.fact = [0] * (maxn + 1)
        self.inv = [0] * (maxn + 1)
        self.finv = [0] * (maxn + 1)

        self.mod = mod

        self.fact[0], self.fact[1] = 1, 1
        self.inv[1] = 1
        self.finv[0], self.finv[1] = 1, 1

        for i in range(2, maxn + 1):
            self.fact[i] = (self.fact[i - 1] * i) % mod
            self.inv[i] = mod - ((self.inv[mod % i] * (mod // i)) % mod)
            self.finv[i] = (self.finv[i - 1] * self.inv[i]) % mod

    def calc(self, n, k):
        return (self.fact[n] * self.finv[k] * self.finv[n - k]) % self.mod


def main():
    MOD = 998244353
    n = int(input())
    p = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        g[p[i]].append(i + 2)
        g[i + 2].append(p[i])
    c = [0] + list(map(int, input().split()))
    d = [0] + list(map(int, input().split()))

    sys.setrecursionlimit(10**9)

    visited = [True] + [False] * n
    bubunn_ccnt = [0] * (n + 1)

    def dfs1(pos):
        visited[pos] = True
        bubunn_ccnt[pos] = c[pos]

        for nex in g[pos]:
            if not visited[nex]:
                dfs1(nex)
                bubunn_ccnt[pos] += bubunn_ccnt[nex]

    dfs1(1)
    # print(bubunn_ccnt)

    visited = [True] + [False] * n
    can_get = [0] * (n + 1)

    def dfs2(pos):
        visited[pos] = True
        can_get[pos] = c[pos]

        for nex in g[pos]:
            if not visited[nex]:
                dfs2(nex)
                can_get[pos] += can_get[nex]
        can_get[pos] -= d[pos]

        if can_get[pos] < 0:
            print(0)
            exit()

    dfs2(1)
    # print(can_get)

    ## https://scrapbox.io/nishio/%E5%B7%A8%E5%A4%A7%E3%81%AAn%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%81%AE%E4%BA%8C%E9%A0%85%E4%BF%82%E6%95%B0
    def naive_comb(n, k, MOD=MOD):
        assert n >= 0
        assert k >= 0
        if n < k:
            return 0
        k = min(k, n - k)
        a = 1
        b = 1
        for i in range(k):
            a *= n - i
            a %= MOD
            b *= i + 1
            b %= MOD
        return (a * pow(b, -1, MOD)) % MOD

    ans = 1
    for i in range(1, n + 1):
        ans *= naive_comb(can_get[i] + d[i], d[i], MOD)

    print(ans)


if __name__ == "__main__":
    main()
