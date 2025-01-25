import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    c = list(input().split())
    d = list(input().split())
    p = list(map(int, input().split()))

    dp = defaultdict(lambda: p[0])
    for i in range(m):
        dp[d[i]] = p[i+1]

    print(sum(dp[cc] for cc in c))
    
if __name__ == '__main__':
    sys.exit(main())
