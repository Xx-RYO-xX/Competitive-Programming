import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        g = defaultdict(list)
        for i in range(n-1):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
        
        dist = defaultdict(lambda :-1)
        dist[1] = 0
        q = deque([1])
        while q:
            pos = q.popleft()
            for nex in g[pos]:
                if dist[nex] == -1:
                    dist[nex] = dist[pos]+1
                    q.append(nex)
        ans = []
        for i in range(2, n+1):
            if dist[i] % k == 0:
                ans.append(dist[i]//k)
            else:
                ans.append(-1)
        print(ans)


if __name__ == '__main__':
    main()
