import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    c1, c2, c3 = list(input())

    print("Won" if c1 == c2 and c2 == c3 and c3 == c1 else "Lost")


if __name__ == "__main__":
    main()
