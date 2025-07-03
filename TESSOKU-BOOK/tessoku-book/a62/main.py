import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    sys.setrecursionlimit(10**9)
    from collections import defaultdict
    
    n, m = map(int, input().split())
    g = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].add(b)
        g[b].add(a)
    
    visited = [True]+[False]*n
    def dfs(pos):
        visited[pos] = True
        for nex in g[pos]:
            if not visited[nex]:
                dfs(nex)
        return
    dfs(1)

    if all(visited):
        print("The graph is connected.")
    else:
        print("The graph is not connected.")

if __name__ == '__main__':
    main()
