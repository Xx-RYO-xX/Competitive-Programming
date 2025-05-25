import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from atcoder.lazysegtree import LazySegTree
    n, q = map(int, input().split())
    
    def op(ele1, ele2):
        return max(ele1, ele2)


    def mapping(func, ele):
        return func + ele

    def composition(func_upper, func_lower):
        return func_upper + func_lower

    e = -float("inf")
    id_ = 0

    seg = LazySegTree(op, e, mapping, composition, id_, [0]*n)
    
    for _ in range(q):
        query = input()
        if query[0] == "1":
            que, pos, x = map(int, query.split())
            pos -=1
            seg.set(pos, x)
        else:
            que, l, r = map(lambda x:int(x)-1, query.split())
            print(seg.prod(l, r))


if __name__ == '__main__':
    main()
