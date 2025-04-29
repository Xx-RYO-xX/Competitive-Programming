import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    dp = [[set() for _ in range(n)] for _ in range(n)]
    dp[0][0].add(a[0][0]%m)
    for i in range(n):
        for j in range(n):
            for r in dp[i][j]:
                if i+1 < n:
                    dp[i+1][j].add((r*10+a[i+1][j])%m)
                if j+1 < n:
                    dp[i][j+1].add((r*10+a[i][j+1])%m)
    
    print(max(dp[n-1][n-1]))

if __name__ == '__main__':
    sys.exit(main())
