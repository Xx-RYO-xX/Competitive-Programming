import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()))

    def is_out_of_range(ii, jj):
        return ii < 0 or jj < 0 or h <= ii or w <= jj

    direction = {(0, -1), (0, 1), (-1, 0), (1, 0)}

    q = deque([])
    visited = set()
    ans = 0

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if not is_out_of_range(ni, nj) and s[ni][nj] == ".":
                        if (ni, nj) in visited:
                            continue

                        b_cnt = 0
                        for ddi, ddj in direction:
                            nni, nnj = ni + ddi, nj + ddj
                            if not is_out_of_range(nni, nnj) and s[nni][nnj] == "#":
                                b_cnt += 1

                        if b_cnt == 1:
                            q.append((ni, nj))
                            visited.add((ni, nj))

    while q:
        nex_q = set()
        while q:
            i, j = q.popleft()

            if s[i][j] == "#":
                continue

            ans += 1
            s[i][j] = "#"

            for di, dj in direction:
                ni, nj = i + di, j + dj
                if not is_out_of_range(ni, nj) and s[ni][nj] == ".":
                    if (ni, nj) not in visited:
                        nex_q.add((ni, nj))
                        visited.add((ni, nj))

        for i, j in nex_q:
            b_cnt = 0
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if not is_out_of_range(ni, nj) and s[ni][nj] == "#":
                    b_cnt += 1

            if b_cnt == 1:
                q.append((i, j))

    print(ans)


if __name__ == "__main__":
    main()
