def main():
    from atcoder.segtree import SegTree
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    for i in range(n):
        p[i] = (p[i], i)

    def minss(num1, num2):
        return min(num1, num2)

    emin = (n + 1, n + 1)

    def maxxx(num1, num2):
        return max(num1, num2)

    emax = (0, 0)

    mins = SegTree(op=minss, e=emin, v=p)
    maxx = SegTree(op=maxxx, e=emax, v=p)

    for _ in range(m):
        l, r = map(int, input().split())

        min_yoso = mins.prod(l - 1, r)
        max_yoso = maxx.prod(l - 1, r)

        mins.set(min_yoso[1], (max_yoso[0], min_yoso[1]))
        mins.set(max_yoso[1], (min_yoso[0], max_yoso[1]))

        maxx.set(min_yoso[1], (max_yoso[0], min_yoso[1]))
        maxx.set(max_yoso[1], (min_yoso[0], max_yoso[1]))

    for i in range(n):
        print(mins.get(i)[0], sep=" ")


if __name__ == "__main__":
    main()
