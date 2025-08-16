import sys


def input():return sys.stdin.readline().rstrip()


def main():
    sys.setrecursionlimit(10**9)
    n, m = map(int, input().split())
    g = list([] for _ in range(n+1))
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    
    ans = [0]*n
    visited = [True]+[False]*n
    def dfs(pos, path_cnt):
        visited[pos] = True

        if path_cnt == n:
            if pos == n:
                ans[path_cnt-1] += 1
            visited[pos] = False
            return
        if pos == n:
            ans[path_cnt-1] += 1
        else:
            for nex in g[pos]:
                if not visited[nex]:
                    dfs(nex, path_cnt+1)
        visited[pos] = False
    
    dfs(1, 1)
    for i in range(1, n):
        print(ans[i], end=" ")


if __name__ == '__main__':
    main()
