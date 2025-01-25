from collections import defaultdict
import sys 


def input():return sys.stdin.readline().rstrip()


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
    n, m = map(int, input().split())
    unit_lst = list()
    for _ in range(m):
        a, b = map(int, input().split())
        unit_lst.append((a, b))
    q = int(input())
    query_lst = list()
    disable = set()
    for _ in range(q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            disable.add(query[1]-1)
        query_lst.append(query)
    
    tetsudou = UnionFind(n+1)
    for i in range(m):
        if i not in disable:
            a, b = unit_lst[i]
            tetsudou.union(a, b)
    # print(tetsudou)
    ans = list()
    for i in range(q)[::-1]:
        query = query_lst[i]
        if query[0] == 1:
            a, b = unit_lst[query[1]-1]
            tetsudou.union(a, b)
        else:
            u, v = query[1], query[2]
            ans.append("Yes" if tetsudou.same(u, v) else "No")
    
    for i in range(len(ans))[::-1]:
        print(ans[i])


if __name__ == '__main__':
    main()
