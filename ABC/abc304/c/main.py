import math


def euclid_distace(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


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
    n, d = map(int, input().split())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    
    virus = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if euclid_distace(xy[i][0], xy[i][1], xy[j][0], xy[j][1]) <= d:
                virus.union(i, j)
    
    for i in range(n):
        if virus.same(0, i):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()