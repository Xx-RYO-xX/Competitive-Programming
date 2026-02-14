import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(a.index(k) + 1 if k in a else -1)


if __name__ == "__main__":
    main()
