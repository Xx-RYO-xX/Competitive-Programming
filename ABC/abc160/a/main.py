import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    print("Yes" if s[2] == s[3] and s[4] == s[5] else "No")


if __name__ == "__main__":
    main()
