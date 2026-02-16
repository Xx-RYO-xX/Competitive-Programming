import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque
    import heapq

    n, m = map(int, input().split())
    if n < m:
        print("No")
        return

    lr = []
    for _ in range(m):
        l, r = map(int, input().split())
        lr.append((l, r))
    lr = deque(sorted(lr))

    rl = []
    heapq.heapify(rl)
    for i in range(1, n + 1):
        while lr and lr[0][0] <= i:
            l, r = lr.popleft()
            heapq.heappush(rl, (r, l))
        if rl and i <= rl[0][0]:
            heapq.heappop(rl)

    print("Yes" if not rl else "No")


if __name__ == "__main__":
    main()
