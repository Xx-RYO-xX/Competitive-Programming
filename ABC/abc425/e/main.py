import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    t, m = map(int, input().split())
    for _ in range(t):
        n = int(input())
        c = list(map(int, input().split()))


if __name__ == "__main__":
    main()
