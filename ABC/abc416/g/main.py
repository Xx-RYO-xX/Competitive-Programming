import sys


def input():return sys.stdin.readline().rstrip()




def main():
    from collections import defaultdict
    
    n, m = map(int, input().split())
    inf = float("inf")
    dist = [[inf] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0

    g = defaultdict(list)
    
    def update_edge(u, v, w):
        for i in range(1, n+1):
            for j in range(1, n+1):
                nd = dist[i][u] + w + dist[v][j]
                if nd < dist[i][j]: dist[i][j] = nd
                nd2 = dist[i][v] + w + dist[u][j]
                if nd2 < dist[i][j]: dist[i][j] = nd2

    # 初期道路の距離更新
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))
        update_edge(a, b, c)

    k, T = map(int, input().split())
    d = list(map(int, input().split()))
    for i in range(k):
        for j in range(i+1, k):
            g[d[i]].append((d[j], T))
            g[d[j]].append((d[i], T))
            update_edge(d[i], d[j], T)

    q = int(input())
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, x, y, t = map(int, query.split())
            update_edge(x, y, t)
        elif query[0] == "2":
            num, x = map(int, query.split())
            for D in d:
                update_edge(x, D, T)
            d.append(x)
        else:
            # 全点間距離の合計を計算
            total = 0
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if dist[i][j] < inf:
                        total += dist[i][j]
            print(total)
if __name__ == '__main__':
    main()
