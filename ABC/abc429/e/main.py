import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    s = ["a"] + list(input())

    dist = [[] for _ in range(n + 1)]
    q = deque()

    for i in range(1, n + 1):
        if s[i] == "S":
            dist[i].append((0, i))
            q.append((i, 0, i))

    while q:
        pos, d, start = q.popleft()

        if len(dist[pos]) >= 2 and d > dist[pos][1][0]:
            continue

        for nex in g[pos]:
            cond = True
            for dd, st in dist[nex]:
                if st == start:
                    cond = False
                    break

            if cond and len(dist[nex]) < 2:
                dist[nex].append((d + 1, start))
                dist[nex].sort()
                q.append((nex, d + 1, start))

    for i in range(1, n + 1):
        if s[i] == "D":
            if len(dist[i]) >= 2:
                ans = dist[i][0][0] + dist[i][1][0]
                print(ans)


if __name__ == "__main__":
    main()
