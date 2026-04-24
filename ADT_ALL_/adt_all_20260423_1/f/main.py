import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n = int(input())
    g = [[]]
    for _ in range(n):
        g.append(list(map(int, input().split())))

    dist = [True] * (n + 1)
    dist[n] = False
    q = deque([n])
    lst = [n]
    while q:
        pos = q.popleft()
        for nex in g[pos][2:]:
            if dist[nex]:
                dist[nex] = False
                lst.append(nex)
                q.append(nex)

    ans = 0
    for ls in lst:
        ans += g[ls][0]
    print(ans)


if __name__ == "__main__":
    main()
