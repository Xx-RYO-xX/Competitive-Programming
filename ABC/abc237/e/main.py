import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import heapq

    n, m = map(int, input().split())
    h = [0] + list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        if h[u] < h[v]:
            g[u].append((v, (h[v] - h[u])))
            g[v].append((u, 0))
        elif h[u] > h[v]:
            g[u].append((v, 0))
            g[v].append((u, h[u] - h[v]))
        else:
            g[u].append((v, 0))
            g[v].append((u, 0))

    inf = float("inf")
    cur = [inf] * (n + 1)
    kakutei = [False] * (n + 1)
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

    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, (h[1] - h[i]) - cur[i])

    print(ans)


if __name__ == "__main__":
    main()
