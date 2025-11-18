import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        que = list(map(int, input().split()))
        if que[0] == 1:
            num, x, y = que
        else:
            num, l, r = que


if __name__ == "__main__":
    main()
