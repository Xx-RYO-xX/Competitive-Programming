import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    ans = 0
    kuro = dict()
    siro = dict()
    for _ in range(q):
        num, rc = map(int, input().split())
        if num == 1:
            r = rc

        else:
            c = rc


if __name__ == "__main__":
    main()
