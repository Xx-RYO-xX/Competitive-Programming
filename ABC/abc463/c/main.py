import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList
    import heapq

    n = int(input())
    takahashi = []
    room = []
    for _ in range(n):
        h, l = map(int, input().split())
        takahashi.append(h)
        room.append((l, h))
    takahashi = SortedList(takahashi)
    heapq.heapify(room)
    q = int(input())
    t = list(map(int, input().split()))
    ans = [0] * q
    t = sorted((val, idx) for idx, val in enumerate(t))

    for tt, idx in t:
        while room and tt >= room[0][0]:
            ll, hh = heapq.heappop(room)
            takahashi.discard(hh)
        ans[idx] = takahashi[-1]
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
