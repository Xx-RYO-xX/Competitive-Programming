import sys


def input():return sys.stdin.readline().rstrip()




def main():
    n, m = map(int, input().split())
    inf = float("inf")
    g = [[inf] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        g[i][i] = 0

    
    def update(x, y, c):
        if c < g[x][y]:
            g[x][y] = c
            g[y][x] = c
        for i in range(1, n+1):
            for j in range(1, n+1):
                nexd = g[i][x]+c+g[y][j]
                if nexd < g[i][j]:
                    g[i][j] = nexd
                nexd2 = g[i][y] +c + g[x][j]
                if nexd2 < g[i][j]:
                    g[i][j] = nexd2

    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))
        edges.append((a, b, c))
    k, T = map(int, input().split())
    d = list(map(int, input().split()))
    for i in range(k):
        for j in range(i+1, k):
            g[d[i]].append((d[j], T))
            g[d[j]].append((d[i], T))

    for x, y, c in edges:
        update(x, y, c)
    for i in range(k):
        for j in range(i+1, k):
            update(d[i], d[j], T)


    q = int(input())
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, x, y, t = map(int, query.split())
            update(x, y, t)
        elif query[0] == "2":
            num, x = map(int, query.split())
            for D in d:
                if T < g[D][x]:
                    update(D, x, T)
            d.append(x)
        else:
            ans = 0
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if g[i][j] < inf:
                        ans += g[i][j]
            print(ans)


if __name__ == '__main__':
    main()
