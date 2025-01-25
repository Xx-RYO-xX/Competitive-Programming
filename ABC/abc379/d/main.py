import sys
from sortedcontainers import SortedList

def input():
    return sys.stdin.readline().rstrip()

def main():
    q = int(input())
    h = SortedList()
    add = 0

    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            h.add(-add)
        elif query[0] == '2':
            t = int(query[1])
            add += t
        elif query[0] == '3':
            H = int(query[1])
            idx = h.bisect_left(H - add)
            count = len(h) - idx
            print(count)
            del h[idx:]

if __name__ == '__main__':
    main()