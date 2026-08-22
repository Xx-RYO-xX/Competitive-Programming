def main():
    import sys

    input = sys.stdin.readline

    for _ in range(int(input())):
        n, m = map(int, input().split())
        g = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, input().split())
            g[a].append(b)
            g[b].append(a)

        dist = [0] * (n + 1)

        from collections import deque

        q = deque([1])
        dist[1] = 1
        oya = [-1] * (n + 1)
        s, t = 0, 0
        while q:
            pos = q.popleft()
            nex_coler = -1 * dist[pos]
            for nex in g[pos]:
                if dist[nex] == 0:
                    dist[nex] = nex_coler
                    q.append(nex)
                    oya[nex] = pos
                elif dist[nex] == nex_coler * -1:
                    s, t = nex, pos
                    break
            else:
                continue
            break

        if s == t == 0:
            print(-1)
            continue

        anss = []
        anst = []
        while s != t:
            anss.append(s)
            anst.append(t)
            s = oya[s]
            t = oya[t]

        anss.append(s)
        ans = anss + anst[::-1]
        print(len(ans))
        print(*ans)


if __name__ == "__main__":
    main()
