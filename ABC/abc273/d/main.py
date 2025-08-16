import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList
    from collections import defaultdict
    
    h, w, R, C = map(int, input().split())
    n = int(input())
    r_to_c = defaultdict(SortedList)
    c_to_r = defaultdict(SortedList)
    
    for _ in range(n):
        r, c = map(int, input().split())
        r_to_c[r].add(c)
        c_to_r[c].add(r)
    
    q = int(input())
    for _ in range(q):
        d, l = map(int, input().split())
        if d == "L":
            


if __name__ == '__main__':
    sys.exit(main())
