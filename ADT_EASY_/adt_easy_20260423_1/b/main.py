import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    print(s[: (len(s) - 1) // 2] + s[(len(s) + 1) // 2 :])


if __name__ == "__main__":
    main()
