import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    for i in range(2 * n + 1):
        if i % 2 != 0:
            print(0, end="")
        else:
            print(1, end="")


if __name__ == "__main__":
    main()
