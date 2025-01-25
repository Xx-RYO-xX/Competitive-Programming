import sys, sys
sys.setrecursionlimit(1 << 25)

def input():
    return sys.stdin.readline().rstrip()

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return 0
        if self.size[fx] < self.size[fy]:
            fx, fy = fy, fx
        self.parent[fy] = fx
        cnt = self.size[fx] * self.size[fy]
        self.size[fx] += self.size[fy]
        return cnt

def main():
    N = int(input())
    edges = []
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    dsu = DSU(N)
    total = 0
    for w, u, v in edges:
        cnt = dsu.union(u, v)
        total += w * cnt
    print(total)

if __name__ == '__main__':
    main()
