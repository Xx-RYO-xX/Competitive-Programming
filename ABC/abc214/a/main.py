import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    if 1 <= n <= 125:
        print(4)
    elif 126 <= n <= 211:
        print(6)
    else:
        print(8)


if __name__ == '__main__':
    main()
