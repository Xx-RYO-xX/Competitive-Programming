import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    h, w = map(int, input().split())
    s = []
    takahashi = None
    gomi = []
    for i in range(h):
        st = list(input())
        for j in range(w):
            if st[j] == "T":
                takahashi = (i, j)
            elif st[j] == "#":
                gomi.append((i, j))
        s.append(st)

    # print(s)

    q = deque([(gomi, 0)])
    visited = set()
    visited.add(tuple(gomi))
    direction = {
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    }
    while q:
        now_gomi, dist = q.popleft()

        if not now_gomi:
            print(dist)
            return

        for di, dj in direction:
            nex_gomi = []
            cond = False

            for i, j in now_gomi:
                ni, nj = i + di, j + dj
                if (ni, nj) == takahashi:
                    cond = True
                    break

                if 0 <= ni < h and 0 <= nj < w:
                    nex_gomi.append((ni, nj))

            if cond:
                continue

            nex_gomi = tuple(nex_gomi)
            if nex_gomi not in visited:
                visited.add(nex_gomi)
                q.append((nex_gomi, dist + 1))

    print(-1)


if __name__ == "__main__":
    main()
