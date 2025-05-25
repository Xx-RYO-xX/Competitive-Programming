import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
        
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))

    T = defaultdict(lambda: float("inf"))
    for i in range(n):
        T[c[i]] = min(T[c[i]], p[i])
    if len(T) < k:
        print(-1)
        return

    print(sum(sorted(T.values())[:k]))


if __name__ == '__main__':
    main()
