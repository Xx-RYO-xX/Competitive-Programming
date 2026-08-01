def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    from collections import defaultdict

    val_idx = defaultdict(lambda: 10**6)
    for i in range(k, n):
        val_idx[a[i]] = min(val_idx[a[i]], i)

    seg = []
    for i, (val, idx) in enumerate(sorted(val_idx.items())):
        seg.append(idx)
        val_idx[val] = i
    vals = sorted(val_idx.keys())

    from atcoder.segtree import SegTree

    def op(val1, val2):
        return min(val1, val2)

    seg = SegTree(op=op, e=10**6, v=seg)

    from bisect import bisect_right

    ans = 10**6
    for i in range(k):
        ii = bisect_right(vals, a[i])
        if ii == len(vals):
            continue
        val = vals[ii]
        idx = seg.prod(val_idx[val], len(vals))
        ans = min(ans, idx - i)

    print(ans if ans != 10**6 else -1)


if __name__ == "__main__":
    main()
