import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    print(a[x - 1])


if __name__ == "__main__":
    main()
