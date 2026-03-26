import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import heapq
    from collections import defaultdict

    n, m, k = map(int, input().split())

    uvw = []
    for _ in range(n):
        u, v, w = map(int, input().split())
        uvw.append((u, v, w))
    t = list(map(int, input().split()))

    g = list([] * (2 * n + 2) for i in range(2 * n + 2))
    for u, v, w in uvw:
        g[u].append((u + n, t[u - 1]))
        g[u + n].append((v, w))
        g[v].append((v + n, t[v - 1]))
        g[v + n].append((u, w))

    g[n] = []
    g[n] = g[n + n]

    # print(g)

    cur = defaultdict(lambda: 10**18)
    kakutei = defaultdict(lambda: False)
    q = []
    cur[n] = 0
    heapq.heappush(q, (cur[n], n))
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

    ans = []
    for pos, dist in cur.items():
        if pos <= n:
            ans.append((dist, pos))

    ans.sort()
    print(cur[ans[k - 1][1]])


if __name__ == "__main__":
    main()
