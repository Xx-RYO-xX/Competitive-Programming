import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import heapq
    from sortedcontainers import SortedList

    n, m = map(int, input().split())
    a = SortedList(map(int, input().split()))
    b = list(map(int, input().split()))

    heapq.heapify(b)

    ans = 0
    while b and a:
        bb = heapq.heappop(b)
        idx = a.bisect_left(bb / 2)
        if idx != len(a) and bb <= a[idx] * 2:
            a.discard(a[idx])
        else:
            break
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
