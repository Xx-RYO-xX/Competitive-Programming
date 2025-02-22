import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, W = map(int, input().split())
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(W+1):
            # if j-w >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j], dp[i][j-w]+v if 0 <= j-w else 0)
            # dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    
    print(dp[n][W])


if __name__ == '__main__':
    main()
