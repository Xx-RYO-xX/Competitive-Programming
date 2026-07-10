from collections import defaultdict

n, m = map(int, input().split())
rigai = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    rigai[a].add(b)
    rigai[b].add(a)

from math import comb

for i in range(1, n + 1):
    print(comb(n - 1 - len(rigai[i]), 3), end=" ")
