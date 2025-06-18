import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from math import prod
    n = int(input())
    a = sorted(map(int, input().split()))
    
    ans = 1
    for i in range(n):
        ans *= a[i]
        # print(a[i])
        if 10**18 < ans:
            print(-1)
            return

    print(ans)

if __name__ == '__main__':
    sys.exit(main())
