import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, x, y = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for i in range(1, n):
        g[i].append(i + 1)
        g[i + 1].append(i)
    g[x].append(y)
    g[y].append(x)
    ans = [0] * n
    for i in range(1, n + 1):
        dist = dict()
        dist[i] = 0
        q = deque([i])
        while q:
            pos = q.popleft()
            for nex in g[pos]:
                if nex not in dist:
                    k = dist[pos] + 1
                    dist[nex] = k
                    ans[k] += 1
                    q.append(nex)

    for val in ans[1:]:
        print(val // 2)


if __name__ == "__main__":
    main()
