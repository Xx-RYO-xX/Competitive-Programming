import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_left
    h, w, n = map(int, input().split())
    a, b = set(), set()
    
    ab = []
    for _ in range(n):
        at, bt = map(int, input().split())
        a.add(at)
        b.add(bt)
        ab.append((at, bt))
    a_lst = sorted(a)
    b_lst = sorted(b)

    for i in range(n):
        a, b = ab[i]
        a_bis = bisect_left(a_lst, a)
        b_bis = bisect_left(b_lst, b)
        print(a-(a_lst[a_bis]-a_bis)+1, b-(b_lst[b_bis]-b_bis)+1)
    
    


if __name__ == '__main__':
    sys.exit(main())
