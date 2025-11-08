import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    n, m, k = map(int, input().split())
    h = SortedList(map(int, input().split()))
    b = SortedList(map(int, input().split()))

    ans = 0
    while b and ans < k:
        max_b = b[-1]

        idx = h.bisect_right(max_b) - 1

        if idx >= 0:
            h.pop(idx)
            b.pop()
            ans += 1
        else:
            b.pop()

    if ans >= k:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
