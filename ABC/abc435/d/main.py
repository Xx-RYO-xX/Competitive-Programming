import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    sys.setrecursionlimit(10**9)
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        g[y].append(x)

    visited = [True] + [False] * n

    def dfs(pos):
        if visited[pos]:
            return False
        visited[pos] = True
        for nex in g[pos]:
            if not visited[nex]:
                if dfs(nex):
                    return True
        return False

    q = int(input())
    for _ in range(q):
        num, v = map(int, input().split())
        if num == 1:
            dfs(v)
        else:
            print("Yes" if visited[v] else "No")


if __name__ == "__main__":
    main()
