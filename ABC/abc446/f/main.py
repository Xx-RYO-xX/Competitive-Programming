import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    gg = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        gg[v].append(u)

    toutatu = set()
    mawari = set()
    queue = deque()
    for k in range(1, n + 1):
        mawari.discard(k)
        for v in g[k]:
            if v > k:
                mawari.add(v)

        if k == 1:
            toutatu.add(1)
        else:
            for u in gg[k]:
                if u in toutatu:
                    queue.append(k)
                    toutatu.add(k)
                    break

        while queue:
            pos = queue.popleft()
            for nex in g[pos]:
                if nex <= k and nex not in toutatu:
                    toutatu.add(nex)
                    queue.append(nex)

        if len(toutatu) == k:
            print(len(mawari))
        else:
            print(-1)


if __name__ == "__main__":
    main()
