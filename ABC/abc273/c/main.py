import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import bisect
    
    n = int(input())
    a = list(map(int, input().split()))
    sa = sorted(set(a))
    
    ans = defaultdict(int)
    # print(sa)
    for A in a:
        k = len(sa)-bisect.bisect_right(sa, A)
        # print(A, k)
        ans[k] += 1
    
    for k in range(n):
        print(ans[k])

if __name__ == '__main__':
    sys.exit(main())
