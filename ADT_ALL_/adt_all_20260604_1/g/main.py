import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, b = map(int, input().split())
        g[u].append((v, b) if u != 1 else (v, b + a[1]))
        g[v].append((u, b) if v != 1 else (u, b + a[1]))

    import heapq

    inf = float("inf")
    cur = [inf] * (n + 1)
    kakutei = [False] * (n + 1)
    prev = [-1] * (n + 1)
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
            nex_dist += a[nex_pos]
            if cur[nex_pos] > cur[pos] + nex_dist:
                cur[nex_pos] = cur[pos] + nex_dist
                heapq.heappush(q, (cur[nex_pos], nex_pos))
                prev[nex_pos] = pos

    print(*cur[2:])


if __name__ == "__main__":
    main()
