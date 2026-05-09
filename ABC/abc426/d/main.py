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

    for _ in range(int(input())):
        n = int(input())
        s = list(input())
        s_rle = runLengthEncode(s)

        cnt0 = s.count("0")
        cnt1 = s.count("1")
        max_len0 = 0
        max_len1 = 0
        for i in range(len(s_rle)):
            if s_rle[i][0] == "0" and max_len0 < s_rle[i][1]:
                max_len0 = s_rle[i][1]
            if s_rle[i][0] == "1" and max_len1 < s_rle[i][1]:
                max_len1 = s_rle[i][1]

        print(min(2 * (cnt0 - max_len0) + cnt1, 2 * (cnt1 - max_len1) + cnt0))


if __name__ == "__main__":
    main()
