import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    if s == "red":
        print("SSS")
    elif s == "blue":
        print("FFF")
    elif s == "green":
        print("MMM")
    else:
        print("Unknown")


if __name__ == "__main__":
    main()
