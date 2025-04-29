import sys


def input():return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split("x"))
    print(a*b)


if __name__ == '__main__':
    main()
