import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, s, t = map(int, input().split())
    a = list(map(int, input().split()))

    print("Yes" if s + sum(a) / 60 <= t else "No")


if __name__ == "__main__":
    main()
