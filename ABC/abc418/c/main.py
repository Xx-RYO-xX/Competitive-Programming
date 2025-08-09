import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate
    import bisect

    n, q = map(int, input().split())
    a = sorted(map(int, input().split()))

    suma = sum(a)
    accma = [0]+list(accumulate(a))


    for _ in range(q):
        b = int(input())
        idx = bisect.bisect_right(a, b-1)
        
        ans = accma[idx]+(n-idx)*(b-1)+1

        print(ans if b<= ans <= suma else -1)


if __name__ == '__main__':
    main()

