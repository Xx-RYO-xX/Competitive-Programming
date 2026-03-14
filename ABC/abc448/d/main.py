import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n = int(input())
    a = [0] + list(map(int, input().split()))
    g = list([] for _ in range(n + 1))
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    visited = [True] + [False] * n
    path = defaultdict(int)
    ans = [False] * (n)
    sys.setrecursionlimit(10**9)

    def dfs(pos, has_same):
        visited[pos] = True
        if path[a[pos]] >= 1 or has_same:
            ans[pos - 1] = True
            has_same = True
        path[a[pos]] += 1
        for nex in g[pos]:
            if not visited[nex]:
                dfs(nex, has_same)
        path[a[pos]] -= 1

    dfs(1, False)
    for ANS in ans:
        print("Yes" if ANS else "No")


if __name__ == "__main__":
    main()
