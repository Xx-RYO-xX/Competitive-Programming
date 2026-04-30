import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()
    AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for S in s:
        print(AZ[(AZ.index(S) + n) % 26], end="")


if __name__ == "__main__":
    main()
