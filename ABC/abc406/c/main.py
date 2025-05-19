import sys
from itertools import groupby


def input(): return sys.stdin.readline().rstrip()


def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    n = int(input())
    p = list(map(int, input().split()))
    if n < 4:
        print(0)
        return

    diff = []
    for i in range(1, n):
        if p[i] > p[i-1]:
            diff.append(1)
        else:
            diff.append(-1)

    rle = runLengthEncode(diff)
    nums = []
    lens = []
    for num, lenss in rle:
        nums.append(num)
        lens.append(lenss)

    ans = 0
    for k in range(len(nums)-2):
        if nums[k] == 1 and nums[k+1] == -1 and nums[k+2] == 1:
            ans += lens[k]*lens[k+2]

    print(ans)


if __name__ == '__main__':
    sys.exit(main())
