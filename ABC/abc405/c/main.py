import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    sums = sum(a)
    ans = 0
    for A in a:
        sums -= A
        ans += A*sums
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
