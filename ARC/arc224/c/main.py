def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)
    for _ in range(int(input())):
        n, m = map(int, input().split())
        g = [[] for _ in range(n + 1)]
        for __ in range(m):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)

        visited = [-1] * (n + 1)

        def dfs(pos):
            a = -1
            for nex in g[pos]:
                a = max(a, visited[nex])
            visited[pos] = a + 1
            for nex in g[pos]:
                if visited[nex] == -1:
                    dfs(nex)

        dfs(1)
        print(*visited[1:])


if __name__ == "__main__":
    main()
