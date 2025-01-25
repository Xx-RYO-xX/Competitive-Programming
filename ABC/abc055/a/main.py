import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(800*n-200*(n//15))


if __name__ == '__main__':
    sys.exit(main())
