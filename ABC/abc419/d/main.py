import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from atcoder.lazysegtree import LazySegTree
    n, m = map(int, input().split())
    s = list(input())
    t = list(input())
    
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
        l -= 1
        seg.apply(l, r, 1)
    
    ans = []
    for i in range(n):
        ans.append(s[i] if seg.get(i)%2==0 else t[i])
    
    print("".join(ans))

if __name__ == '__main__':
    main()
