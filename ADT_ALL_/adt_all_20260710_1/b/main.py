import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(*[i for i in range(1, n + 1)][::-1], sep=",")


if __name__ == "__main__":
    main()
