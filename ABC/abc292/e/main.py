import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from collections import deque

    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)

    ans = 0
    for i in range(1, n + 1):
        dist = defaultdict(lambda: -1)
        dist[i] = 0
        q = deque([i])
        while q:
            pos = q.popleft()
            for nex in g[pos]:
                if dist[nex] == -1:
                    dist[nex] = dist[pos] + 1
                    q.append(nex)
                    ans += 1

    print(ans - m)


if __name__ == "__main__":
    main()
