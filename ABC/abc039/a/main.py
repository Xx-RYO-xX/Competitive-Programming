import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a, b, c = map(int, input().split())
    print(2 * (a * b + b * c + c * a))


if __name__ == "__main__":
    main()
