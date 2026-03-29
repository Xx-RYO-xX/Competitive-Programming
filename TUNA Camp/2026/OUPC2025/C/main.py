import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a, b, c = map(int, input().split())


if __name__ == "__main__":
    main()
