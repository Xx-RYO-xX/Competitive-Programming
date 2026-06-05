from itertools import groupby
import sys


def input():
    return sys.stdin.readline().rstrip()


# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S: str) -> str:
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res


def main():
    s = input()
    print(runLengthEncodeToString(s))


if __name__ == "__main__":
    main()
