import sys
import os


def input():
    return sys.stdin.readline().rstrip()


import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations

    k = int(input())
    ans = set()
    for i in range(1, 9):
        for perm in permutations("TUNACAMP", i):
            ans.add(perm)
    ans = "".join(sorted(ans)[k - 1])
    os.environ["ANS"] = ans
    print(os.environ["ANS"])


if __name__ == "__main__":
    sys.exit(main())
