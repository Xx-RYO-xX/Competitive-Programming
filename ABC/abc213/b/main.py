import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = [(a[i], i+1) for i in range(n)]
    
    ans.sort(reverse=1)
    
    print(ans[1][1])


if __name__ == '__main__':
    sys.exit(main())
