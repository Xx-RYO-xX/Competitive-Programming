import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        one_num = s[0]
        n_num = s[n-1]

        if n_num < one_num:
            print(-1)
            continue

        s = sorted(s)
        taoreru = []
        r = 0
        for i in range(n):
            while r+1 < n and s[r+1]<=2*s[i]:
                r += 1
            taoreru.append(r)

        nx = list(range(n+1))
        def bfs(x):
            if nx[x] != x:
                nx[x] = bfs(nx[x])
            return nx[x]
        dist = [-1]*n
        dq = deque()
        for i in range(n):
            if s[i] == one_num:
                dist[i] = 1
                dq.append(i)
                nx[i] = bfs(i+1)
        
        
        ans = -1
        while dq:
            u = dq.popleft()
            if s[u] == n_num:
                ans = dist[u]
                break
            j = bfs(u+1)
            while j <= taoreru[u]:
                dist[j] = dist[u] + 1
                dq.append(j)
                nx[j] = bfs(j+1)
                j = bfs(j)
        print(ans)

if __name__ == '__main__':
    main()
