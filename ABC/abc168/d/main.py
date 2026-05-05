import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = pos
                q.append(nex)

    print("Yes")
    for i in range(2, n + 1):
        print(dist[i])


if __name__ == "__main__":
    main()
