import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import heapq
    from collections import deque

    q = int(input())
    a_d = deque([])
    a_h = []
    for _ in range(q):
        que = input()
        if que[0] == "1":
            num, x = map(int, que.split())
            a_d.append(x)
        elif que[0] == "2":
            if a_h:
                print(heapq.heappop(a_h))
            else:
                print(a_d.popleft())
        else:
            while a_d:
                heapq.heappush(a_h, a_d.pop())


if __name__ == "__main__":
    sys.exit(main())
