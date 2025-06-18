import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    
    print(sum(1 for A in a if A >= k))


if __name__ == '__main__':
    sys.exit(main())
