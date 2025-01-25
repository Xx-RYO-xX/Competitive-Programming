import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        ans += abs(a[i]-b[i])
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
