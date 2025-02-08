import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate
    from bisect import bisect_right

    n = int(input())
    c = list(accumulate(sorted(map(int, input().split()))))

    q = int(input())
    for _ in range(q):
        x = int(input())
        print(bisect_right(c, x))


if __name__ == '__main__':
    main()
