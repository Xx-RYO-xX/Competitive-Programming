import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    h, w = map(int, input().split())
    s = []
    start = (-1, -1)
    end = (-1, -1)
    for i in range(h):
        st = input()
        for j in range(w):
            if st[j] == "S":
                start = (i, j)
            if st[j] == "G":
                end = (i, j)
        s.append(st)

    direction = [
        (-1, 0, 0),
        (1, 0, 1),
        (0, -1, 2),
        (0, 1, 3),
    ]

    num_to_str = ["U", "D", "L", "R"]

    q = deque([])
    dist = [[[(-1, -1, -1)] * w for _ in range(h)] for _ in range(4)]

    # print(dist)
    x, y = start
    for dx, dy, nd in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#":
            dist[nd][nx][ny] = (x, y, -1)
            q.append((nx, ny, nd))

    while q:
        x, y, d = q.popleft()

        if (x, y) == end:
            ans = []
            bx, by, bd = x, y, d
            while (bx, by) != start:
                ans.append(num_to_str[bd])
                bx, by, bd = dist[bd][bx][by]
            print("Yes")
            print("".join(ans[::-1]))
            return

        for dx, dy, nd in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#":
                if s[x][y] == "o":
                    if nd != d:
                        continue
                if s[x][y] == "x":
                    if nd == d:
                        continue
                if dist[nd][nx][ny] == (-1, -1, -1):
                    dist[nd][nx][ny] = (x, y, d)
                    q.append((nx, ny, nd))

    print("No")


if __name__ == "__main__":
    main()
