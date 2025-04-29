import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a[i] for i in range(n) if i % 2 == 0))


if __name__ == '__main__':
    sys.exit(main())
