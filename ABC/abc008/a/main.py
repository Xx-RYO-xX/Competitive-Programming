import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s, t = map(int, input().split())
    print(t-s+1)


if __name__ == '__main__':
    sys.exit(main())
