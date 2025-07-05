import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    sys.setrecursionlimit(10**9)
    n, m, k = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    
    visited = [False]+[False]*n        
    for _ in range(k):
        p, h = map(int, input().split())
        keibi = defaultdict(lambda: False)
        def dfs(pos, h, depth=0):
            visited[pos] = True
            keibi[pos] = True
            if h <= depth:
                return 
            for nex in g[pos]:
                if not keibi[nex]:
                    dfs(nex, h, depth=depth+1)
        dfs(p, h)

    ans = []
    for i in range(1, n+1):
        if visited[i]:
            ans.append(i)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()
