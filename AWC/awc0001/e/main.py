import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    seg = SegTree(op=max, e=-float("inf"), v=h)
    seg2 = SegTree(op=min, e=float("inf"), v=h)
    ans = 0
    for i in range(n - k + 1):
        ans = max(seg.prod(i, i + k) - seg2.prod(i, i + k), ans)

    print(ans)


if __name__ == "__main__":
    main()
