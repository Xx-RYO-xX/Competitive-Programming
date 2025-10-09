import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    n = int(input())
    a = list(map(int, input().split()))
    for _ in range(int(input())):
        l, r, k = map(int, input().split())


if __name__ == "__main__":
    main()
