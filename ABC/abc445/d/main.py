import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from sortedcontainers import SortedList

    h, w, n = map(int, input().split())
    choko = []
    h_to_i = defaultdict(SortedList)
    w_to_i = defaultdict(SortedList)
    for i in range(n):
        ht, wt = map(int, input().split())
        choko.append((ht, wt))
        h_to_i[ht].add(i)
        w_to_i[wt].add(i)

    ans = [0] * n

    sys.setrecursionlimit(10**9)

    def dfs(hh, ww, r, c):
        if h_to_i[hh]:
            i = h_to_i[hh].pop()
            hi, wi = choko[i]
            w_to_i[wi].remove(i)
            ans[i] = (r + 1, c + 1)
            dfs(hh, ww - wi, r, c + wi)
        elif w_to_i[ww]:
            i = w_to_i[ww].pop()
            hi, wi = choko[i]
            h_to_i[hi].remove(i)
            ans[i] = (r + 1, c + 1)
            dfs(hh - hi, ww, r + hi, c)

    dfs(h, w, 0, 0)

    for ANS in ans:
        print(*ANS)


if __name__ == "__main__":
    main()
