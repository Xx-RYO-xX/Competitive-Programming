import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    r = int(input())
    if r < 1200:
        print("ABC")
    elif r < 2800:
        print("ARC")
    else:
        print("AGC")


if __name__ == "__main__":
    main()
