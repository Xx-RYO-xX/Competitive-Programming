import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque
    import heapq

    n, m = map(int, input().split())
    tutu = []
    tutu_top = []
    heapq.heapify(tutu_top)
    for i in range(n):
        k = int(input())
        a = list(map(int, input().split()))
        tutu.append(deque(a))
        heapq.heappush(tutu_top, (a[0], i))

    while tutu_top:
        color1, i1 = heapq.heappop(tutu_top)
        color2, i2 = heapq.heappop(tutu_top)
        if color1 != color2:
            print("No")
            return

        if len(tutu[i1]) != 0:
            heapq.heappush(tutu_top, (tutu[i1].popleft(), i1))
        if len(tutu[i2]) != 0:
            heapq.heappush(tutu_top, (tutu[i2].popleft(), i2))

    print("Yes")


if __name__ == "__main__":
    main()
