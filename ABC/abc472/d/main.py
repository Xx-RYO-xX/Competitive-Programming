def main():
    import sys

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    s = []
    h_to_w = []
    for _ in range(h):
        st = list(input())[:-1]
        hwt = set()
        for i in range(w):
            if st[i] == "#":
                hwt.add(i)
        h_to_w.append(hwt)
        s.append(st)

    w_to_h = []
    for _ in range(w):
        wht = set()
        for i in range(h):
            if s[i][_] == "#":
                wht.add(i)
        w_to_h.append(wht)

    from collections import deque

    dist = [[-1] * w for _ in range(h)]
    q = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            if (not h_to_w[i]) and (not w_to_h[j]):
                dist[i][j] = 0
                q.append((i, j))
    q = deque(q)

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0)}
    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w:
                if s[ni][nj] == "." and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "." and 0 <= dist[i][j] <= k:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
