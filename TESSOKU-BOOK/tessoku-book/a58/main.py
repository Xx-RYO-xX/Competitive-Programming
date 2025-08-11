import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree
    n, q = map(int, input().split())
    
    seg = SegTree(op=max, e=0, v=[0]*n)
    
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
