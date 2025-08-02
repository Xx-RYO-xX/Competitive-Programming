import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from atcoder.lazysegtree import LazySegTree
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    INF = float("inf")
    ID = INF


    def op(ele1, ele2):
        return ele1 + ele2


    def mapping(func, ele):
        if func == ID:
            return ele
        else:
            return func


    def composition(func_upper, func_lower):
        if func_upper == ID:
            return func_lower
        else:
            return func_upper


    e = 0
    id_ = ID

    seg = LazySegTree(op, e, mapping, composition, id_, a)
    
    MOD = 998244353
    for _ in range(m):
        l, r = map(int, input().split())
        



if __name__ == '__main__':
    main()
