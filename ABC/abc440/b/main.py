import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] = (a[i], i + 1)

    a.sort()
    print(a[0][1], a[1][1], a[2][1])


if __name__ == "__main__":
    main()
