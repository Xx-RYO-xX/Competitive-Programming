import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x = int(input())
    print(int(x ** (1 / 4)))


if __name__ == "__main__":
    main()
