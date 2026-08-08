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

    from collections import deque

    q = deque([1])
    dist = [-1] * (n + 1)
    dist[1] = 0
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                q.append(nex)

    hashi = dist.index(max(dist))

    q = deque([hashi])
    dist = [-1] * (n + 1)
    dist[hashi] = 0
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                q.append(nex)

    print(max(dist) + 1)


if __name__ == "__main__":
    sys.exit(main())
