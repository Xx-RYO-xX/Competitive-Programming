import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    print("Yes" if 3 * a > b * 2 else "No")


if __name__ == "__main__":
    main()
