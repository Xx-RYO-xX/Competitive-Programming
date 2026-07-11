def main():
    import sys

    input = sys.stdin.readline

    from collections import defaultdict

    n, m = map(int, input().split())
    r_c = defaultdict(set)
    c_r = defaultdict(set)
    for _ in range(m):
        r, c = map(int, input().split())
        if r in r_c:
            for cc in r_c.pop(r):
                c_r[cc].discard(r)

        if c in c_r:
            for rr in c_r.pop(c):
                r_c[rr].discard(c)

        r_c[r].add(c)
        c_r[c].add(r)

    ans = 0
    for r, cset in r_c.items():
        ans += len(cset)

    print(ans)


if __name__ == "__main__":
    main()
