import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_right
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        k = int(input())
        


if __name__ == '__main__':
    sys.exit(main())
