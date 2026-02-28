import sys
from collections import defaultdict, deque


def input():
    return sys.stdin.readline().rstrip()


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


def main():
    MOD = 998244353
    n, m = map(int, input().split())
    edge = []
    for i in range(1, m + 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        edge.append((i, u, v))

    uf = UnionFind(n)
    tree = []
    for i, u, v in sorted(edge, reverse=True):
        if not uf.same(u, v):
            uf.union(u, v)
            tree.append((i, u, v))

    tree.sort()
    e_min_i, e_min_u, e_min_v = tree[0]

    tree_no_min = list([] for _ in range(n))
    for i, u, v in tree:
        if i == e_min_i:
            continue
        tree_no_min[u].append(v)
        tree_no_min[v].append(u)

    katagawa = [True] * n
    katagawa[e_min_u] = False
    q = deque([e_min_u])
    while q:
        pos = q.popleft()
        for nex in tree_no_min[pos]:
            if katagawa[nex]:
                katagawa[nex] = False
                q.append(nex)

    ans = 0
    for i, u, v in edge:
        if katagawa[u] != katagawa[v]:
            ans = (ans + pow(2, i, MOD)) % MOD

    print(ans % MOD)


if __name__ == "__main__":
    main()
