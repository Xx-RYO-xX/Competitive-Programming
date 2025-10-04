import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import random

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)}
    sikaku1 = []

    for _ in range(int(input())):
        h, w = map(int, input().split())

        s = []
        brack = []
        for i in range(h):
            st = list(input())
            s.append(st)
            for j in range(w):
                if st == "#":
                    brack.append((i, j))

        ans = 0
        bracked = set()
        for k in range(1000):
            anst = 0
            for i, j in random.sample(brack):
                for di, dj in direction:
                    i += di
                    j += dj


if __name__ == "__main__":
    main()
