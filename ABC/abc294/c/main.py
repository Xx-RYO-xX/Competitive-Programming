import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    from bisect import bisect_left
    
    c = sorted(a+b)

    for i in range(n):
        a[i] = bisect_left(c, a[i])+1
    print(*a)
    
    for i in range(m):
        b[i] = bisect_left(c, b[i])+1
    print(*b)

if __name__ == '__main__':
    sys.exit(main())
