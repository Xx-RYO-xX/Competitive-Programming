from itertools import groupby
import sys


def input():
    return sys.stdin.readline().rstrip()


def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    n, r = map(int, input().split())
    l = list(map(int, input().split()))

    ans = 0

    left = l[:r]
    if 0 in left:
        for i in range(len(left)):
            if left[i] == 0:
                left = left[i:]
                break
        bl = runLengthEncode(left)
        # print(bl)
        for b in bl:
            ans += b[1] * (1 if b[0] == 0 else 2)

    right = l[r:]
    if 0 in right:
        for i in range(len(right) - 1, -1, -1):
            if right[i] == 0:
                right = right[: i + 1]
                break
        al = runLengthEncode(right)
        # print(al)
        for a in al:
            ans += a[1] * (1 if a[0] == 0 else 2)

    print(ans)


if __name__ == "__main__":
    main()
