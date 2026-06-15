import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.lazysegtree import LazySegTree

    def op(ele1, ele2):
        return (ele1[0] + ele2[0], ele1[1] + ele2[1])

    # 区間幅に応じて加算値を乗算
    def mapping(lazy, ele):
        return (lazy * ele[1] + ele[0], ele[1])

    def composition(func_upper, func_lower):
        return func_upper + func_lower

    e = (0, 0)
    id_ = 0

    n, q = map(int, input().split())
    # TODO (初期リストlst)
    seg = LazySegTree(
        op,
        e,
        mapping,
        composition,
        id_,
        [(lst, 1) for lst in [0] + list(map(int, input().split()))],
    )

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            l, r, v = query[1:]
            # print(l, r)
            seg.apply(l, r + 1, v)
        else:
            l, r = query[1:]
            # print(l, r)
            print(seg.prod(l, r + 1)[0])


if __name__ == "__main__":
    main()
