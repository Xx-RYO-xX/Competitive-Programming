import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque, defaultdict

    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(list(input()))

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)}
    s1 = []
    kuro = []
    for i in range(h):
        s1t = []
        for j in range(w):
            if s[i][j] == "#":
                s1t.append(".")
            else:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < h and 0 <= nj < w:
                        if s[ni][nj] == "#":
                            s1t.append("#")
                            kuro.append((i, j))
                            break
                else:
                    s1t.append(".")
        s1.append(s1t)

    dist = list([-1] * w for _ in range(h))
    q = []
    for i, j in kuro:
        dist[i][j] = 0
        q.append((i, j))
    q = deque(q)

    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    for i in range(h):
        for j in range(w):
            print("#" if dist[i][j] != -1 and dist[i][j] % 2 != 0 else ".", end="")
        print()


if __name__ == "__main__":
    main()
