import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque

    n, m = map(int, input().split())
    g = list([] for i in range(n + 1))

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    dist = defaultdict(lambda: -1)
    dist[1] = 0
    q = deque([1])
    f1 = 0
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                f1 = nex
                q.append(nex)

    dist = defaultdict(lambda: -1)
    dist2 = defaultdict(lambda: -1)
    dist[f1] = 0
    q = deque([f1])
    f2 = 0
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                dist2[nex] = dist[pos] + 1
                f2 = nex
                q.append(nex)
            else:
                dist2[nex] = max(dist2[nex], dist[pos] + 1)

    # print(f1, f2)
    ans1 = n + sum(dist2.values())

    # print(ans1)

    dist = defaultdict(lambda: -1)
    dist2 = defaultdict(lambda: -1)
    dist[f2] = 0
    q = deque([f2])
    f2 = 0
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                dist2[nex] = dist[pos] + 1
                f2 = nex
                q.append(nex)
            else:
                dist2[nex] = max(dist2[nex], dist[pos] + 1)

    ans2 = n + sum(dist2.values())

    print(max(ans1, ans2))


if __name__ == "__main__":
    main()
