import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s, t = input().split()

    print("Yes" if s < t else "No")


if __name__ == "__main__":
    sys.exit(main())
