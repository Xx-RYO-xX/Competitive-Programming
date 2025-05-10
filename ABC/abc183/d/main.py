import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from atcoder.lazysegtree import LazySegTree
    n, w = map(int, input().split())
    
    def op(ele1, ele2):
        return max(ele1, ele2)
    def mapping(func, ele):
        return func + ele
    def composition(func_upper, func_lower):
        return func_upper + func_lower
    e = 0
    id_ = 0


    
    s, t, p = [], [], []
    for _ in range(n):
        st, tt, pt = map(int, input().split())
        s.append(st)
        t.append(tt)
        p.append(pt)
    
    seg = LazySegTree(op, e, mapping, composition, id_, [0]*max(t))
    
    for i in range(n):
        seg.apply(s[i], t[i], p[i])
    
    for i in range(max(t)):
        if w < seg.get(i):
            print("No")
            return
    
    print("Yes")
    


if __name__ == '__main__':
    sys.exit(main())
