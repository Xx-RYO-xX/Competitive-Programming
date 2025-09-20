import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    abc = Counter(list(map(int, input().split())))

    print("Yes" if len(abc) <= 2 else "No")


if __name__ == "__main__":
    main()
