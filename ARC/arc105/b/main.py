import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedSet
    n = int(input())
    a = SortedSet(map(int, input().split()))
    while len(a) != 1:
        X = a[-1]
        x = a[0]
        a.pop(-1)
        a.add(X-x)
    print(*a)


if __name__ == '__main__':
    main()
