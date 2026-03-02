import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque, defaultdict

    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0)}
    q = deque([])
    q.append((0, 0, 0))
    visited = defaultdict(lambda: True)
    while q:
        i, j, cnt = q.popleft()
        if i == n - 1 and j == m - 1:
            print(cnt)
            return
        for di, dj in direction:
            ni, nj = di + i, dj + j
            if 0 <= ni < n and 0 <= nj < m and visited[(ni, nj)]:
                visited[(ni, nj)] = False
                if s[ni][nj] == ".":
                    q.appendleft((ni, nj, cnt))
                else:
                    q.append((ni, nj, cnt + 1))


if __name__ == "__main__":
    main()
