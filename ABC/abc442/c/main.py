import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import math

    n, m = map(int, input().split())
    rigai = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        rigai[a].add(b)
        rigai[b].add(a)

    for i in range(1, n + 1):
        print(math.comb(n - 1 - len(rigai[i]), 3), end=" ")


if __name__ == "__main__":
    main()
