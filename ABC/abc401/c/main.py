import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    MOD = 10**9
    n, k = map(int, input().split())
    
    if n < k:
        print(1)
        return

    ans = [1]*k
    next = sum(ans)%MOD
    for i in range(k, n+1):
        ans.append(next)
        next = (next+ans[i]-ans[i-k])%MOD
    
    print(ans[n]%MOD)

if __name__ == '__main__':
    sys.exit(main())
