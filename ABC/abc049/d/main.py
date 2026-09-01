from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return set(i for i in range(self.n) if self.find(i) == root)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

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
    import sys

    input = sys.stdin.readline
    n, k, l = map(int, input().split())
    uf1 = UnionFind(n + 1)
    uf2 = UnionFind(n + 1)
    for _ in range(k):
        p, q = map(int, input().split())
        uf1.union(p, q)
    for _ in range(l):
        r, s = map(int, input().split())
        uf2.union(r, s)

    ans = 0
    cnt = defaultdict(int)

    for i in range(1, n + 1):
        root1 = uf1.find(i)
        root2 = uf2.find(i)
        cnt[(root1, root2)] += 1
    for i in range(1, n + 1):
        root1 = uf1.find(i)
        root2 = uf2.find(i)
        print(cnt[(root1, root2)], end=" ")


if __name__ == "__main__":
    main()
