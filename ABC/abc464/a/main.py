import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()

    print("East" if s.count("E") > s.count("W") else "West")


if __name__ == "__main__":
    main()
