import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(n):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
    s = input()

    dist = dict()
    safe = [[]] * n
    for i in range(n):
        if s[i] == "D":
            q = deque([i])
            dist.clear()
            dist[pos] = 0
            while q:
                pos = q.popleft()
                if s[pos] == "S":
                    safe[i].append(dist[pos])
                else:
                    if len(safe[pos]) == 2:
                if len(safe[i]) == 2:
                    break
                for nex in g[pos]:
                    if nex not in dist:
                        dist[nex] = dist[pos] + 1
                        q.append(nex)


if __name__ == "__main__":
    main()
