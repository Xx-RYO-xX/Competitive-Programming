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
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def main():
    n = int(input())
    tree = UnionFind(n+1)
    jisuu = defaultdict(set)
    for _ in range(n-1):
        u, v = map(int, input().split())
        jisuu[u].add(v)
        jisuu[v].add(u)
        if u != 1 and v != 1:
            tree.union(u, v)
    
    if len(jisuu[1]) == 1:
        print(1)
        exit()
    
    root = tree.roots()
    # print(root)
    
    ans = []
    for R in root[2:]:
        ans.append(tree.size(R))
    
    print(sum(sorted(ans)[:-1])+1)


if __name__ == '__main__':
    main()
