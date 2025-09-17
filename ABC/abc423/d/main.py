import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque
    import heapq

    n, k = map(int, input().split())

    q = deque()
    for i in range(n):
        a, b, c = map(int, input().split())
        q.append((a, b, c, i + 1))

    tennai = []
    heapq.heapify(tennai)
    tennai_num = 0

    now_time = 0
    ans = dict()
    while q:
        a_in, b_in, c_in, i_in = q.popleft()
        now_time = max(a_in, now_time)
        heapq.heappush(tennai, (now_time + b_in, c_in, i_in))
        ans[i_in] = now_time
        tennai_num += c_in

        while q and tennai_num + q[0][2] > k:
            left_time, c_out, i_out = heapq.heappop(tennai)
            tennai_num -= c_out
            now_time = left_time

    for i in range(n):
        print(ans[i + 1])


if __name__ == "__main__":
    main()
