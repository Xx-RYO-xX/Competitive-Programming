import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print("Yes" if m <= sum(a) else "No")


if __name__ == "__main__":
    main()
