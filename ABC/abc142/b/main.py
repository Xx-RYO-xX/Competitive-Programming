import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_left
    n, k = map(int, input().split())
    h = sorted(map(int, input().split()))

    
    print(n-bisect_left(h, k))


if __name__ == '__main__':
    main()
