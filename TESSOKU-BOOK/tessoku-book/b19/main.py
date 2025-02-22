import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, W = map(int, input().split())
    w, v = [], []
    for i in range(n):
        wt, vt = map(int, input().split())
        w.append(wt)
        v.append(vt)
    
    sum_v = sum(v)
    inf = float("inf")
    dp = [[inf]*(sum_v+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(sum_v+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j], dp[i][j-v[i]]+w[i] if 0 <= j-v[i] else inf)
        # print(dp[i])
    print(max(j for j in range(sum_v+1) if dp[n][j] <= W))

if __name__ == '__main__':
    main()
