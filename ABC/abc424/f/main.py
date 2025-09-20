import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from random import randint
    from atcoder.lazysegtree import LazySegTree

    n, q = map(int, input().split())

    INF = 1 << 63

    def op(ele1, ele2):
        return min(ele1, ele2)

    def mapping(func, ele):
        return func + ele

    def composition(func_upper, func_lower):
        return func_upper + func_lower

    e = INF
    id_ = 0

    # TODO (初期リストlst)
    seg = LazySegTree(op, e, mapping, composition, id_, [0] * (n + 1))
    for _ in range(q):
        a, b = map(int, input().split())

        if seg.get(a) == seg.get(b):
            print("Yes")
            seg.apply(a, b + 1, randint(1, 10**9))
        else:
            print("No")


if __name__ == "__main__":
    main()
