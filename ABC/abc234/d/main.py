import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    ans = SortedList()
    for i in range(k - 1):
        ans.add(p[i])

    for i in range(k - 1, n):
        ans.add(p[i])
        print(ans[-k])


if __name__ == "__main__":
    main()
