import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import bisect
    
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        target = 2 * a[i]
        idx = bisect.bisect_left(a, target, lo=i+1)  
        ans += n-idx
    
    print(ans)
    


if __name__ == '__main__':
    sys.exit(main())
