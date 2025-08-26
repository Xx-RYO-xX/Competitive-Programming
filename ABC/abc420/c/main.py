import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    def op(num1, num2):
        return num1 + num2

    seg = SegTree(op=op, e=0, v=list(min(A, B) for A, B in zip(a, b)))
    for _ in range(q):
        c, x, v = input().split()
        x, v = int(x) - 1, int(v)
        if c == "A":
            a[x] = v
        else:
            b[x] = v

        seg.set(x, min(a[x], b[x]))
        print(seg.all_prod())


if __name__ == "__main__":
    main()
