import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    n = int(input())
    x = list(map(int, input().split()))
    densi = defaultdict(list)
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        densi[u].append((v, w))
        densi[v].append((u, w))

    sys.setrecursionlimit(10**7)
    ans = 0
    visited = [False] * n
    def dfs(u):
        nonlocal ans
        visited[u] = True
        sums = x[u]
        for v, w in densi[u]:
            if not visited[v]:
                s = dfs(v)
                ans += abs(s) * w
                sums += s
        return sums

    dfs(0)
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
