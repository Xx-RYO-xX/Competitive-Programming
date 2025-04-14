import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    n, m = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    

    connect = [set() for _ in range(n+1)]
    for i in range(1, n+1):
        for neighbor in graph[i]:
            connect[i].add(neighbor)
    
    for k in range(1, n+1):
        if k == 1:
            ans = len(graph[1])
        else:
            remove = set()
            for i in range(k+1, n+1):
                if any(neighbor <= k for neighbor in connect[i]):
                    remove.add(i)
            
            uf = UnionFind()
            
            for i in range(1, k+1):
                for j in connect[i]:
                    if 1 <= j <= k:  
                        uf.union(i, j)
            
            connected = True
            for i in range(1, k+1):
                if not uf.same(1, i):
                    connected = False
                    break
            
            if connected:
                ans = len(remove)
            else:
                ans = -1
        
        print(ans)


if __name__ == '__main__':
    sys.exit(main())
