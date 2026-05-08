import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    t = int(input())

    direction = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    x, y = 0, 0
    cnt = 0
    for S in s:
        if S in direction:
            dx, dy = direction[S]
            x += dx
            y += dy
        else:
            cnt += 1

    for _ in range(cnt):
        nx = 0 if t == 1 else 10**9
        ny = 0 if t == 1 else 10**9
        for dx, dy in direction.values():
            if t == 1:
                if abs(nx) + abs(ny) < abs(x + dx) + abs(y + dy):
                    nx, ny = x + dx, y + dy
            else:
                if abs(nx) + abs(ny) > abs(x + dx) + abs(y + dy):
                    nx, ny = x + dx, y + dy
        x, y = nx, ny

    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
