import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from atcoder.segtree import SegTree

    n = int(input())
    s = input()

    def op(s1, s2):
        return s1 | s2

    v = []
    for i in range(n):
        v.append(set(s[i]))
    seg = SegTree(op=op, e=set(""), v=v)

    for _ in range(int(input())):
        q, num1, num2 = input().split()
        if q == "1":
            i, c = int(num1), num2
            seg.set(i - 1, set(c))
        else:
            l, r = int(num1), int(num2)
            print(len(seg.prod(l - 1, r)))


if __name__ == "__main__":
    main()
