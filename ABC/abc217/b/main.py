import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    at = set(["ABC", "ARC", "AGC", "AHC"])

    print(*(at - set([s1, s2, s3])))


if __name__ == "__main__":
    sys.exit(main())
