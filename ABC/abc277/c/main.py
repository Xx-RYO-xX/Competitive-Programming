import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n = int(input())
    g = defaultdict(set)
    for _ in range(n):
        a, b = map(int, input().split())
        g[a].add(b)
        g[b].add(a)

    visited = defaultdict(lambda: False)

    sys.setrecursionlimit(10**9)

    def dfs(pos):
        visited[pos] = True

        for nex in g[pos]:
            if not visited[nex]:
                dfs(nex)

    dfs(1)

    ans = 0
    for pos, visit in visited.items():
        if visit:
            ans = max(ans, pos)

    print(ans)


if __name__ == "__main__":
    main()
