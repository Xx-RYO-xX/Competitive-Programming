import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    hen = [() for _ in range(m + 1)]
    hen_to_n = dict()
    for i in range(1, m + 1):
        s, t = map(int, input().split())
        g[s].append(t)
        hen[i] = (s, t)
        hen_to_n[hen[i]] = i

    keiro = set()
    dist = [-1] * (n + 1)
    prev = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])
    toutatu = False
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                prev[nex] = pos
                q.append(nex)
                if nex == n:
                    toutatu = True

    if toutatu:
        now = n
        while now != 1:
            keiro.add(hen_to_n[(prev[now], now)])
            now = prev[now]
    else:
        for i in range(m):
            print(-1)
            return

    # print(toutatu)
    # print(dist)
    # print(keiro)
    anst = dist[n]
    ans = []
    for i in range(1, m + 1):
        if i in keiro:
            dist = [-1] * (n + 1)
            prev = [-1] * (n + 1)
            dist[1] = 0
            q = deque([1])
            toutatu = False
            while q:
                pos = q.popleft()
                if pos == n:
                    toutatu = True
                for nex in g[pos]:
                    if dist[nex] == -1 and (pos, nex) != hen[i]:
                        dist[nex] = dist[pos] + 1
                        prev[nex] = pos
                        q.append(nex)
            if toutatu:
                ans.append(dist[n])
            else:
                ans.append(-1)
        else:
            ans.append(anst)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
