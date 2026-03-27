import sys
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
        return [i for i in range(self.n) if self.find(i) == root]

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


def input():
    return sys.stdin.readline().rstrip()


def main():

    for _ in range(int(input())):
        n = int(input())
        ten_to_ten = defaultdict(set)
        nokori = set([i for i in range(1, n + 1)])
        for i in range(n):
            s = input()
            for j in range(n):
                if s[j] == "1":
                    ii, jj = sorted([i, j])
                    ten_to_ten[ii + 1].add(jj + 1)
                    nokori.discard(ii + 1)
                    nokori.discard(jj + 1)
        uf = UnionFind(n+1)
        for ten1, tenlst in ten_to_ten.items():
            if len(nokori) == 0:
                print(-1)
                break
            chuukei = nokori.pop()
            for ten2 in tenlst:
                if not uf.same(ten1, )
        else:
            continue
        continue


if __name__ == "__main__":
    main()
