import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    nakayosi = defaultdict(set)
    for _ in range(m):
        a = list(map(int, input().split()))
        for i in range(n-1):
            nakayosi[a[i]].add(a[i+1])


if __name__ == '__main__':
    main()
