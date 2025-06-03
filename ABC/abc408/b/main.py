import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = set(map(int, input().split()))
    print(len(a))
    print(*sorted(a))


if __name__ == '__main__':
    sys.exit(main())
