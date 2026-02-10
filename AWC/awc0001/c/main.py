import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    d = sorted(map(int, input().split()))

    print(sum(d[: n - k]))


if __name__ == "__main__":
    main()
