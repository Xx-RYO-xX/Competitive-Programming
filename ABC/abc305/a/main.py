import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(round(n/5)*5)


if __name__ == '__main__':
    main()
