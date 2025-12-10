import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedSet

    n, q = map(int, input().split())
    ans = n
    white = SortedSet()
    white.add((1, n))
    for _ in range(q):
        l, r = map(int, input().split())


if __name__ == "__main__":
    main()
