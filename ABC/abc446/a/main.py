import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    print("Of" + s.lower())


if __name__ == "__main__":
    main()
