import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    print(max(map(int, input().split())))


if __name__ == '__main__':
    sys.exit(main())
