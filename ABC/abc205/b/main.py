import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    
    print("Yes" if a == list(range(1, n+1)) else "No")
    


if __name__ == '__main__':
    sys.exit(main())
