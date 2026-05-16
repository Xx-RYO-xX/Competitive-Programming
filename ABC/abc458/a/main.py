import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    n = int(input())
    print(s[n:-n])


if __name__ == "__main__":
    main()
