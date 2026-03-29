import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(max(n - 10, 1))


if __name__ == "__main__":
    main()
