import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0)}
    for i in range(h):
        for j in range(w):
            cnt = 0
            for dx, dy in direction:
                nx, ny = i + dx, j + dy
                if 0 <= nx < h and 0 <= ny < w:
                    cnt += 1
            print(cnt, end=" ")

        print()


if __name__ == "__main__":
    main()
