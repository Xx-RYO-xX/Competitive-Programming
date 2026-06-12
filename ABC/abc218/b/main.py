import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    p = list(map(int, input().split()))

    az = "abcdefghijklmnopqrstuvwxyz"

    for i in range(26):
        print(az[p[i] - 1], end="")


if __name__ == "__main__":
    main()
