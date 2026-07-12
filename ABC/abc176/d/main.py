def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    ch, cw = map(lambda x: int(x) - 1, input().split())
    dh, dw = map(lambda x: int(x) - 1, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()))

    direction = {
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    }

    mahou = set()
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (i, j) not in direction and (i, j) != (0, 0):
                mahou.add((i, j))

    dist = [[-1] * w for _ in range(h)]
    dist[ch][cw] = 0
    q = deque([(ch, cw, 0)])
    while q:
        now_h, now_w, cnt = q.popleft()

        if (now_h, now_w) == (dh, dw):
            print(cnt)
            return

        for ddh, ddw in direction:
            nex_h, nex_w = now_h + ddh, now_w + ddw
            if (
                0 <= nex_h < h
                and 0 <= nex_w < w
                and (dist[nex_h][nex_w] == -1 or dist[nex_h][nex_w] > 0)
                and s[nex_h][nex_w] == "."
            ):
                dist[nex_h][nex_w] = 0
                q.appendleft(((nex_h, nex_w, cnt)))

        for ddh, ddw in mahou:
            nex_h, nex_w = now_h + ddh, now_w + ddw
            if (
                0 <= nex_h < h
                and 0 <= nex_w < w
                and dist[nex_h][nex_w] == -1
                and s[nex_h][nex_w] == "."
            ):
                dist[nex_h][nex_w] = cnt + 1
                q.append(((nex_h, nex_w, cnt + 1)))

    print(-1)


if __name__ == "__main__":
    main()
