import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import combinations
    from math import lcm

    n, m, y = map(int, input().split())
    a = map(int, input().split())

    ans = set()

    for comb in combinations(a, m):
        anst = lcm(*comb)

    print(len(ans))


if __name__ == "__main__":
    main()
