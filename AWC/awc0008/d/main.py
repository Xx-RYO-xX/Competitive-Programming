import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import heapq

    n, m = map(int, input().split())
    fd = []
    for i in range(n):
        f, d = map(int, input().split())
        fd.append((-1 * f, d, 1))

    heapq.heapify(fd)

    anst = 0
    ans = 0
    for _ in range(m):
        f, d, k = heapq.heappop(fd)
        anst += -1 * f
        ans = max(ans, anst)
        ff = max((-1 * f) - d, 0)
        heapq.heappush(fd, (-1 * ff, d, k + 1))
    print(ans)


if __name__ == "__main__":
    main()
