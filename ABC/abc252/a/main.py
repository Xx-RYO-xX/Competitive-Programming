import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    print(chr(n))


if __name__ == "__main__":
    main()
