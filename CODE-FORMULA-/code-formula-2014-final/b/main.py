import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ans = 0
    if n % 2 == 0:
        ans = 3*n//2 - 2*(n//2)
    else:
        # print(3*((n//2)+1), 2*(n//2))
        ans = 3*((n//2)+1) - 2*(n//2)
    print(ans)


if __name__ == '__main__':
    main()
