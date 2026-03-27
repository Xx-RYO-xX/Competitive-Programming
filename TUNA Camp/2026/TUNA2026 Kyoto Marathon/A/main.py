import sys


def input():
    return sys.stdin.readline().rstrip()


def greedy(m, t):
    p = [m]
    pp = set([i for i in range(m)])
    now = m
    for i in range(m):
        nex = 0
        nex_val = 10**18
        for ppp in pp:
            if nex_val > t[now][ppp]:
                nex = ppp
                nex_val = t[now][ppp]
        pp.discard(nex)
        p.append(nex)
        now = nex
    return p + [m]


def calc_score(m, t, c, p):
    sums = 0
    for i in range(m + 1):
        sums += t[p[i]][p[i + 1]]

    return max(c - sums, 1)


def main():
    import time
    import random

    start = time.time()

    n, m, k, c = map(int, input().split())
    t = []
    for _ in range(m + 1):
        t.append(list(map(int, input().split())))
    s = []
    for _ in range(n):
        s.append(int(input()))

    p = greedy(m=m, t=t)
    now_score = calc_score(m, t, c, p)

    while time.time() - start < 1.85:
        l, r = sorted([random.randint(1, m + 1), random.randint(1, m + 1)])
        if r - l <= 1:
            continue
        np = p[:]
        np[l:r] = np[l:r][::-1]
        nex_score = calc_score(m, t, c, np)
        if now_score < nex_score:
            now_score = nex_score
            p = np[:]

    print(p[0])
    for i in range(1, m + 1):
        print(p[i], p[i])
    print(p[-1])


if __name__ == "__main__":
    main()
