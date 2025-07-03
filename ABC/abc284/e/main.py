import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    sys.setrecursionlimit(10**9)
    
    n, m = map(int, input().split())
    g = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)
    
    limit = 1000000
    visited = [True]+[False]*n
    path = []
    ans = 0
    def dfs(pos):
        nonlocal ans
        visited[pos] = True
        path.append(pos)
        ans += 1
        if ans == limit:
            return True
        for nex in g[pos]:
            if not visited[nex]:
                if dfs(nex):
                    return True
        visited[pos] = False
        path.pop()
        return False
    dfs(1)
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
