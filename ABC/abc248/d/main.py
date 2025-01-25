import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from sortedcontainers import SortedList
    import bisect
    
    n = int(input())
    a = list(map(int, input().split()))
    
    d = defaultdict(SortedList)
    for i in range(n):
        d[a[i]].add(i+1)
    
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        l_idx = bisect.bisect_left(d[x], l)
        r_idx = bisect.bisect_right(d[x], r)
        
        print(r_idx-l_idx)


if __name__ == '__main__':
    main()
