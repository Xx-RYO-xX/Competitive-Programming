import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w, n = map(int, input().split())
    t = list(input())
    s = []
    for _ in range(h):
        s.append(list(input()))

    direction = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    ans = 0
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if s[i][j] == "#":
                continue
            ni, nj = i, j
            for T in t:
                di, dj = direction[T][::-1]
                ni += di
                nj += dj
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == ".":
                    continue
                else:
                    break
            else:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
