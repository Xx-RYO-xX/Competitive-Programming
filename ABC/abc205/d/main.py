import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_left

    n, q = map(int, input().split())
    a = sorted(set(map(int, input().split())))
    m = [a[i] - (i+1) for i in range(len(a))]
    for _ in range(q):
        k = int(input())
        pos = bisect_left(m, k)
        if pos == 0:
            print(k)
        else:
            print(a[pos-1] + (k-m[pos-1]))
        


if __name__ == '__main__':
    sys.exit(main())
