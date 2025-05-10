import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    x = int(input())
    print(x if x >= 0 else 0)


if __name__ == '__main__':
    sys.exit(main())
