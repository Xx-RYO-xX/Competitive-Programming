import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import heapq
    
    n, m = map(int, input().split())
    g = defaultdict(set)
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].add((b, c))
        g[b].add((a, c))
    
    inf = float("inf")
    cur = defaultdict(lambda: inf)
    kakutei = defaultdict(lambda: False)
    q = []
    cur[1] = 0
    heapq.heappush(q, (cur[1], 1))
    while q:
        pos = heapq.heappop(q)[1]
        if kakutei[pos]:
            continue
        kakutei[pos]= True
        for nex in g[pos]:
            nex_pos, nex_dist = nex
            if cur[nex_pos] > cur[pos]+nex_dist:
                cur[nex_pos] = cur[pos]+nex_dist
                heapq.heappush(q, (cur[nex_pos], nex_pos))
    
    for i in range(1, n+1):
        if cur[i] == inf:
            print(-1)
        else:
            print(cur[i])


if __name__ == '__main__':
    main()
