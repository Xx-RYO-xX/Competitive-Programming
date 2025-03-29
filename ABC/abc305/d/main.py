import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_left
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]*n
    for i in range(1, n):
        s[i] = s[i-1]
        if i % 2 == 1:
            s[i] += a[i] - a[i-1]

    def f(x):
        idx = bisect_left(a, x)
        if idx == 0:
            return 0
        res = s[idx-1]
        if idx % 2 == 1:
            res += x - a[idx-1]
        return res

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(f(r) - f(l))

if __name__ == '__main__':
    main()
