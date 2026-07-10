n = int(input())
xy = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
xy.append((0, 0))

from math import sqrt

ans = 0
for i in range(n + 1):
    a, b = xy[i]
    c, d = xy[i + 1]
    ans += sqrt((a - c) ** 2 + (b - d) ** 2)

print(ans)
