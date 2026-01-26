import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    print(s.count("i") + s.count("j"))


if __name__ == "__main__":
    main()
