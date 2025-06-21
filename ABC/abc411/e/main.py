import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    MOD = 998244353
    for _ in range(n):
        a = list(map(int, input().split()))


if __name__ == '__main__':
    main()
