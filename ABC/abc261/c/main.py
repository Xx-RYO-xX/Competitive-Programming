import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n = int(input())
    s = defaultdict(int)
    for _ in range(n):
        ss = input()
        if ss not in s:
            print(ss)
        else:
            print(ss + "(" + str(s[ss]) + ")")
        s[ss] += 1


if __name__ == "__main__":
    main()
