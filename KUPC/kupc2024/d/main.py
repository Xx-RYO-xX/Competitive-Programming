import sys 
from collections import defaultdict


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
    n = int(input())
    x_to_y = defaultdict(set)
    y_to_x = defaultdict(set)
    zahyou_to_num = defaultdict(int)
    juuhuku = defaultdict(list)
    # num_to_zahyou = defaultdict(tuple)
    for i in range(n):
        x, y = map(int, input().split())
        x_to_y[x].add(y)
        y_to_x[y].add(x)
        if (x, y) not in zahyou_to_num:
            zahyou_to_num[(x, y)] = i
        else:
            juuhuku[(x, y)].append(i)
        # num_to_zahyou[i+1] = (x, y)
    # print(zahyou_to_num)
    # print(num_to_zahyou)
    # print(juuhuku)
    
    jirai = UnionFind(n)
    for zahyou in zahyou_to_num:
        x, y = zahyou
        for Y in x_to_y[x]:
            jirai.union(zahyou_to_num[zahyou], zahyou_to_num[(x, Y)])
            
            if zahyou in juuhuku:
                for num in juuhuku[zahyou]:
                    jirai.union(zahyou_to_num[zahyou], num)
                juuhuku.pop(zahyou)
        x_to_y.pop(x)
        for X in y_to_x[y]:
            jirai.union(zahyou_to_num[zahyou], zahyou_to_num[X, y])
            
            if zahyou in juuhuku:
                for num in juuhuku[zahyou]:
                    jirai.union(zahyou_to_num[zahyou], num)
                juuhuku.pop(zahyou)
        y_to_x.pop(y)

    ans = []
    for root in jirai.roots():
        ans.append(jirai.size(root))
    
    print(sum(sorted(ans)[-2:])+1)

if __name__ == '__main__':
    sys.exit(main())
