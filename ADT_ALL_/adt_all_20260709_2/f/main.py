from collections import deque

n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(2 * n + 2)]
for i in range(n):
    ii = i + 1
    g[a[i]].append(2 * ii)
    g[a[i]].append(2 * ii + 1)

dist = [-1] * (2 * n + 2)
dist[1] = 0
q = deque([1])
while q:
    pos = q.popleft()
    for nex in g[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            q.append(nex)

print(*dist[1:], sep="\n")
