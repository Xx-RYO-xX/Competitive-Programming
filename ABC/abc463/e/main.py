import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, y = map(int, input().split())
    g = [[] for _ in range(n + 1 + 2)]
    for _ in range(m):
        u, v, t = map(int, input().split())
        g[u].append((v, t))
        g[v].append((u, t))
    x = map(int, input().split())
    for idx, X in enumerate(x, start=1):
        g[idx].append((-2, X))
        g[-1].append((idx, X))
    g[-2].append((-1, y))

    import heapq

    inf = float("inf")
    cur = [inf] * (n + 1 + 2)
    kakutei = [False] * (n + 1 + 2)
    q = []
    cur[1] = 0
    heapq.heappush(q, (cur[1], 1))
    while q:
        pos = heapq.heappop(q)[1]
        if kakutei[pos]:
            continue
        kakutei[pos] = True
        for nex in g[pos]:
            nex_pos, nex_dist = nex
            if cur[nex_pos] > cur[pos] + nex_dist:
                cur[nex_pos] = cur[pos] + nex_dist
                heapq.heappush(q, (cur[nex_pos], nex_pos))

    for i in range(2, n + 1):
        print(cur[i], end=" ")


if __name__ == "__main__":
    main()
