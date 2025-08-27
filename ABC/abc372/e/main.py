import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [[-1, [i]] for i in range(n)]

    def find(self, x):
        if self.parents[x][0] < 0:
            return x
        else:
            self.parents[x][0] = self.find(self.parents[x][0])
            return self.parents[x][0]

    def plus(self, x):
        root = self.find(x)
        return self.parents[root][1]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x][0] > self.parents[y][0]:
            x, y = y, x

        self.parents[x][0] += self.parents[y][0]
        a = self.parents[x][1][-10:]
        b = self.parents[y][1][-10:]

        merged = sorted(set(a + b))

        self.parents[x][1] = merged[-10:]

        self.parents[y][0] = x
        self.parents[y][1] = []

    def size(self, x):
        return -self.parents[self.find(x)][0]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents[0]) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def main():
    n, q = map(int, input().split())
    uf = UnionFind(n + 1)

    for _ in range(q):
        que, u, v = map(int, input().split())
        if que == 1:
            uf.union(u, v)
        else:
            ans = uf.plus(u)
            if v <= len(ans):
                print(ans[len(ans) - v])
            else:
                print(-1)


if __name__ == "__main__":
    sys.exit(main())
