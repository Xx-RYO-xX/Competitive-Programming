def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()[:-1]))
    direction = {
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    }
    # print(s)
    hana = set()
    ans = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                kouho = [(i, j)]
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < h
                        and 0 <= nj < w
                        and s[ni][nj] == "#"
                        and (ni, nj) not in hana
                    ):
                        kouho.append((ni, nj))
                if len(kouho) == 5:
                    ans.append((i + 1, j + 1))
                    for ii, jj in kouho:
                        hana.add((ii, jj))

    print(len(ans))
    for i, j in ans:
        print(i, j)


if __name__ == "__main__":
    main()
