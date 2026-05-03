import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b, t = map(int, input().split())

    print(b * (t // a))


if __name__ == "__main__":
    main()
