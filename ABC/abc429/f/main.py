import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    n = int(input())
    s = []
    for _ in range(3):
        s.append(list(input()))

    q = int(input())
    for _ in range(q):
        r, c = map(int, input().split())


if __name__ == "__main__":
    main()
