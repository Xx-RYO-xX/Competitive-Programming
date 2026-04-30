import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    for i in range(1, n + 1):
        print("x" if i % 3 == 0 else "o", end="")


if __name__ == "__main__":
    main()
