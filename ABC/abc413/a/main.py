import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = sum(map(int, input().split()))
    
    print("Yes" if a <= m else "No")
    


if __name__ == '__main__':
    main()
