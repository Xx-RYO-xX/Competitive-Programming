import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    seg = SegTree(op=max, e=0, v=a)
    for _ in range(q):
        l, r = map(int, input().split())
        print(seg.prod(l - 1, r))


if __name__ == "__main__":
    main()
