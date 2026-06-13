import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    az = "abcdefghijklmnopqrstuvwxyz"

    for S in s:
        if S not in az:
            print(S, end="")


if __name__ == "__main__":
    main()
