import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    for _ in range(int(input())):
        h, w = map(int, input().split())
        s = []
        for i in range(h):
            s.append(list(input()))

        direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
        mirror = {
            "A": {
                "L": (0, -1, "L"),
                "R": (0, 1, "R"),
                "U": (-1, 0, "U"),
                "D": (1, 0, "D"),
            },
            "B": {
                "R": (1, 0, "D"),
                "D": (0, 1, "R"),
                "L": (-1, 0, "U"),
                "U": (0, -1, "L"),
            },
            "C": {
                "R": (-1, 0, "U"),
                "U": (0, 1, "R"),
                "L": (1, 0, "D"),
                "D": (0, -1, "L"),
            },
        }

        q = deque()
        q.append((0, 0, 0, "R"))

        visited = {}

        ans = float("inf")
        while q:
            now_h, now_w, cost, muki = q.popleft()

            if now_h == h - 1 and now_w == w and muki == "R":
                ans = min(ans, cost)
                continue

            if now_h < 0 or now_h >= h or now_w < 0 or now_w >= w:
                continue

            key = (now_h, now_w, muki)
            if key in visited and visited[key] <= cost:
                continue
            visited[key] = cost

            now_type = s[now_h][now_w]

            for mirror_type in ["A", "B", "C"]:
                dh, dw, nex_muki = mirror[mirror_type][muki]

                nh, nw = now_h + dh, now_w + dw

                nex_cost = cost + (0 if mirror_type == now_type else 1)

                if mirror_type == now_type:
                    q.appendleft((nh, nw, nex_cost, nex_muki))
                else:
                    q.append((nh, nw, nex_cost, nex_muki))

        print(ans)


if __name__ == "__main__":
    main()
