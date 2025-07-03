import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    sys.setrecursionlimit(10**9)
    
    n, m = map(int, input().split())
    g = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].add(b)
        g[b].add(a)
    
    visited = [True]+[False]*n
    path = []
    def dfs(pos):
        visited[pos] = True
        path.append(pos)
        if pos == n:
            return True
        for nex in g[pos]:
            if not visited[nex]:
                if dfs(nex):
                    return True
        path.pop()
        return False
    
    dfs(1)
    print(*path)




if __name__ == '__main__':
    main()
