import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += a[i]*a[j]
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
