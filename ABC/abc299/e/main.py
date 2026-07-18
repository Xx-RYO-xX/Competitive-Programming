from posixpath import sep
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque, defaultdict

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    k = int(input())
    s = [1] * (n + 1)
    kuro_lst = []
    kuro = []
    dist = defaultdict(lambda: -1)
    q = deque()
    for _ in range(k):
        p, d = map(int, input().split())

        kuro = []
        dist.clear()
        q.clear()
        dist[p] = 0
        q = deque([p])
        while q:
            pos = q.popleft()
            if dist[pos] == d:
                kuro.append(pos)
                continue
            s[pos] = 0
            for nex in g[pos]:
                if dist[nex] == -1:
                    dist[nex] = dist[pos] + 1
                    q.append(nex)
        kuro_lst.append(kuro)

    for kuro in kuro_lst:
        for pos in kuro:
            if s[pos] == 1:
                break
        else:
            print("No")
            return

    print("Yes")
    print(*s[1:], sep="")


if __name__ == "__main__":
    main()
