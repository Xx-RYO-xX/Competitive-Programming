import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print("Yes" if -(2**31) <= n < 2**31 else "No")


if __name__ == "__main__":
    main()
