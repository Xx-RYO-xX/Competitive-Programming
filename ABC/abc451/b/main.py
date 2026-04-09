import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, m = map(int, input().split())
    pre = defaultdict(int)
    nex = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        pre[a] += 1
        nex[b] += 1

    for i in range(1, m + 1):
        print(nex[i] - pre[i])


if __name__ == "__main__":
    main()
