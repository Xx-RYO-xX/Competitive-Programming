import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    seg = SegTree(op=lambda x, y: x + y, e=0, v=a)

    ans = 0
    for i in range(n - k + 1):
        if seg.prod(i, i + k) <= 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
