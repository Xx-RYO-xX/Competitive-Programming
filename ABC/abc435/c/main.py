import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    i = 0
    max_can = 1
    while i < min(max_can, n):
        max_can = max(max_can, i + a[i])
        i += 1

    print(i)


if __name__ == "__main__":
    main()
