import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque
    
    n, m = map(int, input().split())
    g = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].add(b)
        g[b].add(a)
    
    dist = defaultdict(lambda :-1)
    dist[1] = 0
    q = deque([1])
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos]+1
                q.append(nex)
    for i in range(1, n+1):
        print(dist[i])

if __name__ == '__main__':
    main()
