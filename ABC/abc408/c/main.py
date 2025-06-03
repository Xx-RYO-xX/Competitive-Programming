import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    from atcoder.lazysegtree import LazySegTree
    def op(ele1, ele2):
        return min(ele1, ele2)
    def mapping(func, ele):
        return func + ele
    def composition(func_upper, func_lower):
        return func_upper + func_lower
    e = float("inf")
    id_ = 0
    seg = LazySegTree(op, e, mapping, composition, id_, [0]*n)
    
    for _ in range(m):
        l, r = map(int, input().split())
        seg.apply(l-1, r, 1)
    print(seg.prod(0, n))


if __name__ == '__main__':
    sys.exit(main())
