import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    n, l = map(int, input().split())
    d = list(map(int, input().split()))

    dist_to_player = {}

    for i in range(n):
        dist_to_player[d[i]] = i + 1

    q = int(input())
    sorted_d = SortedList(d)

    dist = 0
    for _ in range(q):
        query = input()

        if query[0] == "1":
            que, x, m = map(int, query.split())

            sorted_d.discard(d[x-1])
            sorted_d.add(d[x-1] + m)
            dist_to_player.pop(d[x-1])
            dist_to_player[d[x-1] + m] = x
            d[x-1] += m
        else:
            for i in range(1, 6):
                print(dist_to_player[sorted_d[-i]], sorted_d[-i] + dist)

        dist += l


if __name__ == '__main__':
    main()
