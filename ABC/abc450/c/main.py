import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque

    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()))

    visited = [[False] * w for _ in range(h)]

    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def bfs(i, j):
        q = deque([(i, j)])
        res = True
        while q:
            i, j = q.popleft()
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                res = False
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == ".":
                    if not visited[ni][nj]:
                        q.append((ni, nj))
                        visited[ni][nj] = True

        return res

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "." and not visited[i][j]:
                if bfs(i, j):
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
