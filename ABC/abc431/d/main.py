import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    whb = []
    for _ in range(n):
        whb.append(tuple(map(int, input().split())))


if __name__ == "__main__":
    main()
