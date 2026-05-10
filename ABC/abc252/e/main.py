import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import heapq

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    hen_to_num = dict()
    for i in range(1, m + 1):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))
        hen_to_num[tuple(sorted((a, b)))] = i

    inf = float("inf")
    cur = [inf] * (n + 1)
    kakutei = [False] * (n + 1)
    prev = [-1] * (n + 1)
    q = []
    cur[1] = 0
    heapq.heappush(q, (cur[1], 1))
    while q:
        pos = heapq.heappop(q)[1]
        if kakutei[pos]:
            continue
        kakutei[pos] = True
        for nex in g[pos]:
            nex_pos, nex_dist = nex
            if cur[nex_pos] > cur[pos] + nex_dist:
                cur[nex_pos] = cur[pos] + nex_dist
                heapq.heappush(q, (cur[nex_pos], nex_pos))
                prev[nex_pos] = pos

    ans = []
    for i in range(2, n + 1):
        prev_pos = prev[i]
        ans.append(hen_to_num[tuple(sorted((prev_pos, i)))])

    print(*ans)


if __name__ == "__main__":
    main()
