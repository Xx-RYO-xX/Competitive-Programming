import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, h, m = map(int, input().split())
    
    dp = [-float("inf")] * (h+1)
    dp[0] = 0
    sumb = 0
    for i in range(n):
        a, b = map(int, input().split())
        sumb += b
        for j in range(h, a-1, -1):
            dp[j] = max(dp[j], dp[j-a]+b)

        tairyoku = sumb - m  
        if tairyoku > 0 and max(dp) < tairyoku:
            print(i)
            return
    print(n)
    

if __name__ == '__main__':
    sys.exit(main())
