import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    MOD = 10**9 + 7
    
    n = int(input())
    ans = 1
    for i in range(n):
        ans *= i+1
        ans %= MOD
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
