import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    s = Counter(input()).items()

    s = sorted(s, key=lambda x: (-x[1], x[0]))
    print(s[0][0])


if __name__ == "__main__":
    main()
