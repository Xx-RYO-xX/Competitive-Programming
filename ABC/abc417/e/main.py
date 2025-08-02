import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedSet
    from collections import defaultdict
    sys.setrecursionlimit(10**9)
    
    for _ in range(int(input())):
        n, m, x, y = map(int, input().split())
        g = defaultdict(SortedSet)
        for  i in range(m):
            u, v = map(int, input().split())
            g[u].add(v)
            g[v].add(u)
        
        visited = [True]+[False]*n
        path = []
        def dfs(pos):
            visited[pos] = True
            path.append(pos)
            if pos == y:
                return True
            for nex in g[pos]:
                if not visited[nex]:
                    if dfs(nex):
                        return True
            path.pop()
            return False
        dfs(x)
        print(*path)


if __name__ == '__main__':
    main()
