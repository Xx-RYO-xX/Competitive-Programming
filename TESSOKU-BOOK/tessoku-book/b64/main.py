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
    prev = defaultdict(lambda:-1)
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
                prev[nex_pos] = pos
    
    if cur[n] == inf:
        print(-1)
        return

    path = []
    node = n
    while node != -1:
        path.append(node)
        node = prev[node]
    print(*path[::-1])

if __name__ == '__main__':
    main()
