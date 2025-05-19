import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    cal = 1
    for i in range(n):
        cal *= a[i]
        
        if k < len(str(cal)):
            cal = 1
    
    print(cal)


if __name__ == '__main__':
    sys.exit(main())
