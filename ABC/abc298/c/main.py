import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from sortedcontainers import SortedSet, SortedList
    n = int(input())
    q = int(input())
    box_card = defaultdict(SortedList)
    card_box = defaultdict(SortedSet)
    for _ in range(q):
        query = input()
        if query[0] == "1":
            Q, i, j = map(int, query.split())
            box_card[j].add(i)
            card_box[i].add(j)
        
        if query[0] == "2":
            Q, i = map(int, query.split())
            print(*box_card[i])
        
        if query[0] == "3":
            Q, i = map(int, query)
            print(*card_box[i])


if __name__ == '__main__':
    main()
