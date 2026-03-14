import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] < x:
            x = a[i]
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
