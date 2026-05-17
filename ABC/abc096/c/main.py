import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()))

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0)}

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                cnt = 0
                for dx, dy in direction:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < h and 0 <= ny < w:
                        cnt += s[nx][ny] == "#"
                if cnt == 0:
                    print("No")
                    return

    print("Yes")


if __name__ == "__main__":
    main()
