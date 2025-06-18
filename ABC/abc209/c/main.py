import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    MOD = 10**9+7
    
    n = int(input())
    c = sorted(list(map(int, input().split())))    
    
    ans = c[0]
    for i in range(1, n):
        ans *= c[i] - i
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
