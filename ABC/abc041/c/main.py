import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = []
    for i in range(n):
        ans.append((a[i], i+1))
    
    ans.sort(reverse=True)
    for i in range(n):
        print(ans[i][1])


if __name__ == '__main__':
    main()
