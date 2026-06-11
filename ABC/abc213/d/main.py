import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    for i in range(1, n + 1):
        g[i].sort()

    visited = [True] + [False] * n

    sys.setrecursionlimit(10**9)

    def dfs(pos):
        print(pos, end=" ")
        visited[pos] = True

        for nex in g[pos]:
            if not visited[nex]:
                dfs(nex)
                print(pos, end=" ")

    dfs(1)


if __name__ == "__main__":
    sys.exit(main())
