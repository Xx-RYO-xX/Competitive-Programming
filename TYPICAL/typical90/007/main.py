import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_right
    n = int(input())
    a = sorted(map(int, input().split()))
    # print(a)
    q = int(input())
    for _ in range(q):
        b = int(input())
        idx = bisect_right(a, b)
        # print(idx)
        ans = min(abs(a[idx%n]-b), abs(a[(idx-1)%n]-b))
        print(ans)



if __name__ == '__main__':
    sys.exit(main())
