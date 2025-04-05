import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        print(sum(a[7*i:7*i+7]), end=" ")

if __name__ == '__main__':
    main()
