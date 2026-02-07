import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, l, s, t = map(int, input().split())
    g = list([] for i in range(n + 1))
    for _ in range(m):
        u, v, c = map(int, input().split())
        g[u].append((v, c))

    ans = set()

    sys.setrecursionlimit(10**9)

    def dfs(pos, dep=0, cost_sum=0):
        if dep == l:
            if s <= cost_sum <= t:
                ans.add(pos)
            return
        for nex, cost in g[pos]:
            dfs(nex, dep=dep + 1, cost_sum=cost_sum + cost)

    dfs(1)
    print(*sorted(ans), sep=" ")


if __name__ == "__main__":
    main()
