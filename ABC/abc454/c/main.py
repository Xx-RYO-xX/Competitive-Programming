import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)

    visited = [True] + [False] * n

    sys.setrecursionlimit(10**9)

    def dfs(pos):
        visited[pos] = True
        for nex in g[pos]:
            if not visited[nex]:
                if dfs(nex):
                    return True
        return False

    dfs(1)

    print(visited.count(True) - 1)


if __name__ == "__main__":
    main()
