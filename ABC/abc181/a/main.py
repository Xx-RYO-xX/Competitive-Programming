import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print("White" if n % 2 == 0 else "Black")


if __name__ == "__main__":
    main()
