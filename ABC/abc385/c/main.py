import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    h = list(map(int, input().split()))
    
    building = defaultdict(list)
    for i in range(n):
        building[h[i]].append(i)
    
    ans = 1
    for B in building:
        lst = building[B]
        m = len(lst)
        if m < 2:
            ans = max(ans, m)
            continue

        dp = [defaultdict(lambda:1) for _ in range(m)]
        for j in range(m):
            for i in range(j):
                diff = lst[j] - lst[i]
                dp[j][diff] = dp[i][diff] + 1
                ans = max(ans, dp[j][diff])
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
