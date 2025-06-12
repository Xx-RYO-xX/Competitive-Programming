import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    for A in a:
        if A %2 == 0:
            print(A, end=" ")


if __name__ == '__main__':
    sys.exit(main())
