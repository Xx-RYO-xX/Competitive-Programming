import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = list(input())

    moji = {"O": 0, "D": 0, "I": 1, "Z": 2, "S": 5, "B": 8}
    for S in s:
        print(moji[S] if S in moji else S, end="")
    print()


if __name__ == "__main__":
    main()
