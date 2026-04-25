import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    from math import comb

    n = int(input())
    s = input()

    a = [0]
    b = [0]
    c = [0]
    for S in s:
        a.append(a[-1] + 1 if S == "A" else a[-1])
        b.append(b[-1] + 1 if S == "B" else b[-1])
        c.append(c[-1] + 1 if S == "C" else c[-1])

    ab = []
    bc = []
    ca = []

    abc = []

    for i in range(n + 1):
        ab.append(a[i] - b[i])
        bc.append(b[i] - c[i])
        ca.append(c[i] - a[i])

        abc.append((a[i] - b[i], b[i] - c[i]))

    abcnt = Counter(ab)
    bccnt = Counter(bc)
    cacnt = Counter(ca)
    abccnt = Counter(abc)

    ans = 0

    cnt = [abcnt, bccnt, cacnt, abccnt]

    for i in range(4):
        for val in cnt[i].values():
            if val > 1:
                if i == 3:
                    ans -= 2 * comb(val, 2)
                else:
                    ans += comb(val, 2)

    print((n * (n + 1) // 2) - ans)


if __name__ == "__main__":
    main()
