import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, d = map(int, input().split())
    print("Yes" if a <= d else "No")


if __name__ == "__main__":
    main()
