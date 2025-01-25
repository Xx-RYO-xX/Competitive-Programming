import sys


def input():return sys.stdin.readline().rstrip()

def X(a, b):
    return (a**2)*b

def main():
    INF = float("inf")
    n, m = map(int, input().split())
    dp = list([1, 1] for i in range(m))

    A = list(list(map(int, input().split())) for _ in range(n))
    for j in range(m):
        if A[0][j] != 0:
            dp[j][0] += A[0][j]
        else:
            dp[j][1] += 1
    # print(dp)
    
    for i in range(1, n):
        ndp = list([0, 0] for i in range(m))
        exit_cond = []
        for j in range(m):
            if A[i][j] != 0:
                ndp[j][0] += A[i][j]
            else:
                ndp[j][1] += 1
            # dp_x = list(X(dp[i][0]+ndp[j][0], dp[i][1]+ndp[j][1]) for i in range(m))
            dp_x = []
            for k in range(m):
                a, b = dp[k][0], dp[k][1]
                na, nb = ndp[j][0], ndp[j][1]
                if na + a <= 0:
                    dp_x.append(-INF)
                else:
                    dp_x.append(X(na+a, nb+b))

            # print(dp_x)
            if max(dp_x) == min(dp_x) == -INF:
                exit_cond.append(True)
            else:
                exit_cond.append(False)
            
            idx_max = dp_x.index(max(dp_x))
            ndp[j][0] += dp[idx_max][0]
            ndp[j][1] += dp[idx_max][1]
    
        if all(exit_cond):
            print(-1)
            exit()
        dp = ndp[:]
        # print(dp)
    
    print(max(X(dp[i][0], dp[i][1]) for i in range(m)))


if __name__ == '__main__':
    main()
