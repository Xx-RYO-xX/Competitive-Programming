import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b, c, d = map(int, input().split())
    if (c >= a) and (d < b):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
