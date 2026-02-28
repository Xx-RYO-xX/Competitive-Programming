import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    s = input()
    cnt = Counter(s)
    maxs = max(cnt.values())
    for S in s:
        if cnt[S] != maxs:
            print(S, end="")


if __name__ == "__main__":
    main()
