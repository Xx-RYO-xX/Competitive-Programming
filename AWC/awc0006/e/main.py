import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n, q = map(int, input().split())
    s = list(map(int, input().split()))

    seg = SegTree(op=lambda a, b: a + b, e=0, v=s)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que, l, r = query
            print(seg.prod(l - 1, r))
        else:
            que, x, v = query
            seg.set(x - 1, v)


if __name__ == "__main__":
    main()
