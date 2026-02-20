import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    print(n if n % 2 == 0 else 2 * n)


if __name__ == "__main__":
    main()
