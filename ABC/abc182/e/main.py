import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    h, w, n, m = map(int, input().split())

    masu = []
    for _ in range(h):
        tmp = []
        for __ in range(w):
            tmp.append([False, False])
        masu.append(tmp)
    ab = []
    for _ in range(n):
        a, b = map(lambda x: int(x) - 1, input().split())
        ab.append((a, b))
    cd = set()
    for _ in range(m):
        c, d = map(lambda x: int(x) - 1, input().split())
        cd.add((c, d))

    for a, b in ab:
        for i in range(2):
            masu[a][b][i] = True
            for j in [1, -1]:
                ta, tb = a, b
                if i == 0:
                    tb += j
                else:
                    ta += j
                while (
                    0 <= ta < h
                    and 0 <= tb < w
                    and (ta, tb) not in cd
                    and not masu[ta][tb][i]
                ):
                    masu[ta][tb][i] = True
                    if i == 0:
                        tb += j
                    else:
                        ta += j

    ans = 0
    for i in range(h):
        for j in range(w):
            if (i, j) not in cd:
                ans += any(masu[i][j])

    print(ans)


if __name__ == "__main__":
    main()
