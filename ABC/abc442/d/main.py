import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    seg = SegTree(op=lambda x, y: x + y, e=0, v=a)

    for _ in range(q):
        query = input()
        match query[0]:
            case "1":
                que, x = map(lambda x: int(x) - 1, query.split())
                ax = seg.get(x)
                ax1 = seg.get(x + 1)
                seg.set(x, ax1)
                seg.set(x + 1, ax)
            case "2":
                que, l, r = map(int, query.split())
                print(seg.prod(l - 1, r))


if __name__ == "__main__":
    main()
