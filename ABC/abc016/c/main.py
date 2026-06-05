import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    for i in range(1, n + 1):
        dist = [-1] * (n + 1)
        dist[i] = 0
        q = deque([i])
        while q:
            pos = q.popleft()
            for nex in g[pos]:
                if dist[nex] == -1:
                    dist[nex] = dist[pos] + 1
                    q.append(nex)
        print(dist.count(2))


if __name__ == "__main__":
    main()
