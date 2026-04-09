import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import heapq

    q = int(input())
    niwa = []
    heapq.heapify(niwa)
    for _ in range(q):
        num, h = map(int, input().split())
        if num == 1:
            heapq.heappush(niwa, h)
        else:
            while niwa and niwa[0] <= h:
                heapq.heappop(niwa)

        print(len(niwa))


if __name__ == "__main__":
    main()
