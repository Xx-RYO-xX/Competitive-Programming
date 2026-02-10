import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    k = int(input())
    print(k + 1)


if __name__ == "__main__":
    main()
