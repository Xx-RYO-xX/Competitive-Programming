import sys
import heapq


def input():return sys.stdin.readline().rstrip()


def dijkstra(g, start):
    """各頂点までの最短距離を求める dijkstra の実装"""
    dist = {}
    hq = [(0, start)]
    while hq:
        d, u = heapq.heappop(hq)
        if u in dist:
            continue
        dist[u] = d
        for v, w in g[u]:
            if v not in dist:
                heapq.heappush(hq, (d + w, v))
    return dist


def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b, t = map(int, input().split())
        g[a].append((b, t))
        g[b].append((a, t))
    
    inf = float("inf")
    ans = inf
    for i in range(1, n+1):
        dist = dijkstra(g, i)
        worst = max(dist.values()) if len(dist) == n else inf
        ans = min(ans, worst)
    
    print(ans)

if __name__ == '__main__':
    main()
