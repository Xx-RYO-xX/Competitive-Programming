import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    if s[-2:] == "er":
        print("er")
    elif s[-3:] == "ist":
        print("ist")


if __name__ == "__main__":
    main()
