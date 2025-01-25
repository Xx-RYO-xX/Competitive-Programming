import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    sa = 0
    for i in range(n):
        sa += abs(a[i]-b[i])
    if k < sa:
        print("No")
        return
    print("Yes" if (k - sa) % 2 == 0 else "No")
    


if __name__ == '__main__':
    sys.exit(main())
