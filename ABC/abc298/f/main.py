import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n = int(input())
    rr = defaultdict(int)
    cc = defaultdict(int)
    masu = dict()
    for _ in range(n):
        r, c, x = map(int, input().split())
        rr[r] += x
        cc[c] += x
        masu[(r, c)] = x
    # print(rr)
    # print(cc)
    rr = sorted([(val, key) for key, val in rr.items()], reverse=True)
    cc = sorted([(val, key) for key, val in cc.items()], reverse=True)

    ans = 0
    for rval, rkey in rr:
        for cval, ckey in cc:
            if (rkey, ckey) not in masu:
                ans = max(ans, rval + cval)
                break
            else:
                ans = max(ans, rval + cval - masu[(rkey, ckey)])

    print(ans)


if __name__ == "__main__":
    main()
