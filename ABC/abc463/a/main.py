import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y = map(int, input().split())

    print("Yes" if 9 * x == 16 * y else "No")


if __name__ == "__main__":
    main()
