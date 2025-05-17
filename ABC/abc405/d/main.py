import sys


def input():return sys.stdin.readline().rstrip()


def print_2d(lst, sep=None):
    """
    2次元配列を出力する関数

    Parameters
    ----------
    lst : list
        出力したい2次元配列
    sep : str
        区切り文字(デフォルトはNone)
    """
    for LIST in lst:
        print(*LIST, sep=sep)




def main():
    from collections import deque
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    esc = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == "E":
                esc.append((i, j))

    if not esc:
        print_2d(s, sep="")
        return

    dist = [[-1]*w for _ in range(h)]
    q = deque()
    
    for i, j in esc:
        dist[i][j] = 0
        q.append((i, j))
    
    direction = [(0, 1, ">"), (1, 0, "v"), (0, -1, "<"), (-1, 0, "^")]
    while q:
        i, j = q.popleft()
        for di, dj, arrow in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and s[ni][nj] != "#" and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    

    inf = float("inf")
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans_arrow = None
                min_dist = inf
                
                for di, dj, arrow in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < h and 0 <= nj < w and dist[ni][nj] != -1:
                        if dist[ni][nj] < min_dist:
                            min_dist = dist[ni][nj]
                            ans_arrow = arrow
                
                s[i][j] = ans_arrow

    print_2d(s, sep="")

if __name__ == "__main__":
    sys.exit(main())