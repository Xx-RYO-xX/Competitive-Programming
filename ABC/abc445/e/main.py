import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree
    from math import lcm

    def op(n1, n2):
        return lcm(n1, n2) % mod

    mod = 998244353
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))

        seg = SegTree(op=op, e=1, v=a)
        for i in range(n):
            li = lcm(seg.prod(0, i), seg.prod(i + 1, n))
            print(li, end=" ")
        print()


if __name__ == "__main__":
    main()
