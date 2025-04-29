import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate
    from bisect import bisect_left
    n, q = map(int, input().split())
    a = sorted(map(int, input().split()))
    accm = [0] + list(accumulate(a))
    for _ in range(q):
        x = int(input())
        k = bisect_left(a, x)
        left = x*k-accm[k]
        right = (accm[n]-accm[k])-x*(n-k)
        print(left+right)


if __name__ == '__main__':
    sys.exit(main())
