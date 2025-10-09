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
        # print(s_rle)
        max_len = 0
        max_youso = None
        pop = 0
        for i in range(len(s_rle)):
            if max_len < s_rle[i][1]:
                max_len = s_rle[i][1]
                max_youso = s_rle[i]
                pop = i
        # print(max_len, max_youso)
        # print(pop)
        s_rle.pop(pop)
        # print(s_rle)

        ans = 0
        for S in s_rle:
            if S[0] == max_youso[0]:
                ans += 2 * S[1]
            else:
                ans += S[1]
        print(ans)


if __name__ == "__main__":
    main()
