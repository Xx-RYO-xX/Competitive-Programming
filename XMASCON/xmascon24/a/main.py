from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    color = [-1]*(n+1)
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        while queue:
            v = queue.popleft()
            for nx in graph[v]:
                if color[nx] < 0:
                    color[nx] = color[v] ^ 1
                    queue.append(nx)
                elif color[nx] == color[v]:
                    return False
        return True

    ok = True
    for i in range(1, n+1):
        if color[i] < 0:
            if not bfs(i):
                ok = False
                break
    print(1 if ok else 0)
