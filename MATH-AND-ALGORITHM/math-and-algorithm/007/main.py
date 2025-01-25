import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, x, y = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i % x == 0:
            ans += 1
        elif i % y == 0:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()
