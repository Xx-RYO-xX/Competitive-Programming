import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(2**n - 2 * n)


if __name__ == "__main__":
    main()
