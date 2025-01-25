import sys
from collections import defaultdict

def input():return sys.stdin.readline().rstrip()

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
    n = int(input())
    kai = UnionFind()
    kai_lst = set()
    for _ in range(n):
        a, b = map(int, input().split())
        kai.union(a, b)
        kai_lst.add(a)
        kai_lst.add(b)
    kai_lst = sorted(kai_lst, reverse=True)
    for K in kai_lst:
        if kai.same(1, K):
            print(K)
            exit()

    print(1)

if __name__ == '__main__':
    main()
