import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    seg1 = SegTree(op=max, e=-float("inf"), v=a)
    seg2 = SegTree(op=min, e=float("inf"), v=a)

    for _ in range(q):
        l, r = map(int, input().split())
        print(seg1.prod(l - 1, r) - seg2.prod(l - 1, r))


if __name__ == "__main__":
    main()
