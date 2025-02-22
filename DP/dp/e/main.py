import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    VALUE = 10**5+1
    n, W = map(int, input().split())
    dp = [[float("inf")]*VALUE for i in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(VALUE):
            dp[i+1][j] = dp[i][j] 
            if j >= v:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-v]+w)

        # print(dp[i])
    print(max(j for j in range(VALUE) if dp[n][j] <= W))

if __name__ == '__main__':
    main()
