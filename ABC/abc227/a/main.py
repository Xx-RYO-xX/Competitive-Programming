import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, k, a = map(int, input().split())
    print((a+k-1)%n if (a+k-1)%n != 0 else n)


if __name__ == '__main__':
    main()
