import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    i, j = 0, 0
    ans = 0
    while i < (n+1)//2 and j < n:
        if a[i] * 2 <= a[j]:
            ans += 1
            i += 1
            j += 1
        else:
            j += 1
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
