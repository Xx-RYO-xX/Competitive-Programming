import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()

    print(s.lstrip("o"))


if __name__ == "__main__":
    main()
