import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree
    n, b, q = map(int, input().split())
    a = list(map(lambda x: (int(x), 1), input().split()))
    
    def op(l, r):
        l_sum, l_cnt = l
        r_sum, r_cnt = r
        return (l_sum+r_sum, l_cnt+r_cnt)
    
    seg = SegTree(op=op, e=(0, 0), v=a)
    
    def f(val):
        sums, cnt = val
        if cnt == 0:
            return True
        return sums < b*cnt
    
    for _ in range(q):
        c, x = map(int, input().split())
        seg.set(c-1, (x, 1))
    
        idx = seg.max_right(0, f=f)
        ans = seg.prod(0, idx+1 if idx != n else idx)
        print(ans[0]/ans[1])



if __name__ == '__main__':
    main()
