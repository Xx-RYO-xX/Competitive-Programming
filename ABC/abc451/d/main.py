import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    sys.setrecursionlimit(10**9)

    def explore(v, mx, vv):
        if v > 0:
            vv.add(v)

        e = 0
        while True:
            p = 1 << e
            w = int(str(v) + str(p)) if v > 0 else p
            if w <= mx:
                explore(w, mx, vv)
            else:
                break
            e += 1

    vv = set()
    explore(0, 10**9, vv)
    ans = sorted(vv)

    print(ans[n - 1])


if __name__ == "__main__":
    main()
