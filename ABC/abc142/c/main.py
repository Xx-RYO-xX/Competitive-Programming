import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = []
    for i in range(1, n+1):
        ans.append((a[i-1], i))
    
    ans.sort()

    for i in range(n):
        print(ans[i][1], end=" ")


if __name__ == '__main__':
    main()
