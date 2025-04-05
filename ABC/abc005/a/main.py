import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x, y = map(int, input().split())
    print(y//x)


if __name__ == '__main__':
    sys.exit(main())
