def main():
    import sys

    input = sys.stdin.readline

    q, v = map(int, input().split())
    import heapq

    juuden = []
    heapq.heapify(juuden)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            t, w = query[1:]
            heapq.heappush(juuden, -(w - t))
        else:
            t = query[1]
            if juuden:
                anst = heapq.heappop(juuden)
                if -anst + t < 0:
                    print(-1)
                    heapq.heappush(juuden, anst)
                else:
                    print(min(v, -anst + t))
            else:
                print(-1)


if __name__ == "__main__":
    main()
