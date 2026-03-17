import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    import heapq

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    aa = Counter(a)
    vv = []
    for i in range(1, m + 1):
        heapq.heappush(vv, (aa[i], i))

    for _ in range(m):
        cnt, v = heapq.heappop(vv)
        a.append(v)
        heapq.heappush(vv, (cnt + 1, v))

    # print(a)

    # for _ in range(2 * m):
    #     cnt, v = heapq.heappop(vv)
    #     a.append(v)
    #     heapq.heappush(vv, (cnt + 1, v))

    # print(a)

    q = int(input())
    for _ in range(q):
        x = int(input())
        if x < len(a):
            print(a[x - 1])
        else:
            print((a[-1] + x - len(a) - 1) % m + 1)


if __name__ == "__main__":
    main()
