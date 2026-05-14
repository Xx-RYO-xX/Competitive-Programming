import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    h, w, m = map(int, input().split())
    h_w = defaultdict(set)
    w_h = defaultdict(set)
    for _ in range(m):
        h1, w1 = map(int, input().split())
        h_w[h1].add(w1)
        w_h[w1].add(h1)

    w_len_max = 0
    for hh, ww in h_w.items():
        if len(ww) > w_len_max:
            w_len_max = len(ww)

    h_maxs = []
    for hh, ww in h_w.items():
        if len(ww) == w_len_max:
            h_maxs.append(hh)

    h_len_max = 0
    for ww, hh in w_h.items():
        if len(hh) > h_len_max:
            h_len_max = len(hh)

    w_maxs = []
    for ww, hh in w_h.items():
        if len(hh) == h_len_max:
            w_maxs.append(ww)

    ans = len(h_w[h_maxs[0]]) + len(w_h[w_maxs[0]])
    for www in w_maxs:
        for hhh in h_maxs:
            if www not in h_w[hhh]:
                print(ans)
                return

    print(ans - 1)


if __name__ == "__main__":
    main()
