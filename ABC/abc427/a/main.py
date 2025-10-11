import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    s.pop(int((len(s) + 1) / 2) - 1)
    print(*s, sep="")


if __name__ == "__main__":
    main()
