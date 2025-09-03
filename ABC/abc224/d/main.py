import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque

    m = int(input())
    g = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)
    p = list(map(int, input().split()))
    s = [0] * 9

    for i in range(8):
        s[p[i] - 1] = i + 1

    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    if s == goal:
        print(0)
        return

    goal = tuple(goal)

    dist = defaultdict(lambda: -1)
    dist[tuple(s)] = 0
    q = deque([tuple(s)])
    while q:
        pos = q.popleft()
        nex_lst = []

        idx_0 = pos.index(0)
        for i in range(9):
            if i != idx_0:
                if idx_0 + 1 in g[i + 1]:
                    nex_c = list(pos[:])
                    nex_c[idx_0] = pos[i]
                    nex_c[i] = 0
                    nex_lst.append(tuple(nex_c))

        for nex in nex_lst:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                if nex == goal:
                    print(dist[nex])
                    return
                q.append(nex)

    print(-1)


if __name__ == "__main__":
    main()
