import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s, ss = map(int, input().split("-"))
    # print(s, ss)

    if ss != 8:
        print(s, "-", ss + 1, sep="")
    else:
        print(s + 1, "-", 1, sep="")


if __name__ == "__main__":
    main()
