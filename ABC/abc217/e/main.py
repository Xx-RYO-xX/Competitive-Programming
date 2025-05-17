import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import heapq
    q = int(input())
    a = heapq.heapify([])
    for _ in range(q):
        query = input()
        if query[0] == "1":
            que, x = map(int, input().split())
            heapq.heappush(a, x)

        elif query[1] == "2":
            
        else:
            


if __name__ == '__main__':
    sys.exit(main())
