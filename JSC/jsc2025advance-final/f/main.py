import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import heapq

    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    g = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    inf = float("inf")
    for i in range(1, n + 1):
        cur = defaultdict(lambda: inf)
        kakutei = defaultdict(lambda: False)
        q = []
        cur[1] = 0
        heapq.heappush(q, (cur[i], w[i - 1]))
        while q:
            print(q)
            pos = heapq.heappop(q)[1]
            if kakutei[pos]:
                continue
            kakutei[pos] = True
            for nex in g[pos]:
                print(nex)
                nex_pos, nex_dist = nex
                nex_dist += w[nex_pos - 1]
                if cur[nex_pos] > cur[pos] + nex_dist:
                    cur[nex_pos] = cur[pos] + nex_dist
                    heapq.heappush(q, (cur[nex_pos], nex_pos))

        print(cur[i])


if __name__ == "__main__":
    main()
