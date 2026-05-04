import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    l, q = map(int, input().split())
    ki = SortedList([0, l])
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            ki.add(x)
        else:
            idx = ki.bisect_left(x)
            print(ki[idx] - ki[idx - 1])


if __name__ == "__main__":
    sys.exit(main())
