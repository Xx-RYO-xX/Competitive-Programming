import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque

    n = int(input())
    g = [[] for _ in range(n + 1)]
    jisuu = defaultdict(int)
    num_to_ab = dict()
    for i in range(1, n):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
        jisuu[a] += 1
        jisuu[b] += 1
        num_to_ab[i] = sorted([a, b])

    k = max(jisuu.values())

    visited = [True] + [False] * n

    ab_to_c = dict()

    def dfs(pos):
        visited[pos] = True

        for nex in g[pos]:
            if not visited[nex]:
                dfs(nex)


if __name__ == "__main__":
    main()
