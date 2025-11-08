import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, b = map(int, input().split())

    print(h - b if h - b >= 0 else 0)


if __name__ == "__main__":
    main()
