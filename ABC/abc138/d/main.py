def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    ans = [0] * (n + 1)
    for _ in range(q):
        p, x = map(int, input().split())
        ans[p] += x

    visited = [False] * (n + 1)

    sys.setrecursionlimit(10**9)

    def dfs(pos, before):
        visited[pos] = True
        ans[pos] += ans[before]

        for nex in g[pos]:
            if not visited[nex]:
                dfs(nex, pos)

    dfs(1, 0)

    print(*ans[1:])


if __name__ == "__main__":
    main()
