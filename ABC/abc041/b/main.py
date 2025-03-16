import sys


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    MOD = 10**9 + 7
    print((a*b*c)%MOD)


if __name__ == '__main__':
    main()
