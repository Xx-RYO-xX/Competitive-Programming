import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, T = map(int, input().split())
    t = list(map(int, input().split()))
    
    ans = 0
    for i in range(1, n):
        ans += min(T, t[i]-t[i-1])
    
    print(ans+T)


if __name__ == '__main__':
    sys.exit(main())
