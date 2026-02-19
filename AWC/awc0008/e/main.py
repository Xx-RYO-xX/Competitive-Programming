import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n = int(input())
    a = list(map(int, input().split()))

    seg = SegTree(op=lambda x, y: x + y, e=0, v=[0] * (max(a) + 1))
    ans = 0

    for i in range(n)[::-1]:
        val = a[i]
        ans += seg.prod(0, val)
        seg.set(val, seg.get(val) + 1)

    print(ans)


if __name__ == "__main__":
    main()
