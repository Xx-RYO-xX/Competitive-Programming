import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList
    n, q = map(int, input().split())
    not_called = SortedList(range(1, n+1))
    called = SortedList()
    for _ in range(q):
        event = input()
        if event[0] == "1":
            called.add(not_called.pop(0))
        elif event[0] == "2":
            num, x = map(int, event.split())
            called.discard(x)
        else:
            print(called.pop(0))
            

if __name__ == '__main__':
    sys.exit(main())
