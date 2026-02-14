import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    print("Yes" if s[0] == s[-1] else "No")


if __name__ == "__main__":
    main()
