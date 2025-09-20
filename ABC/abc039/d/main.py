import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input().split()))

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)}

    ans = s[:]
    for i in range(h):
        for j in range(w):
            for dx, dy in direction:
                ni, nj = i + dx, j + dy


if __name__ == "__main__":
    main()
