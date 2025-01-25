import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    MOD = 1000000007
    n = int(input())
    a = list(input().split())

    ans = ""
    for i in range(n):
        ans += a[i]
    # print(ans)
    print(int(ans)%MOD)

if __name__ == '__main__':
    main()
