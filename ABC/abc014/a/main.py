import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = int(input())
    b = int(input())
    print(b - a % b if a % b != 0 else 0)


if __name__ == "__main__":
    main()
