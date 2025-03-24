import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    
    for L in l:
        if a[L-1] != n and a[L-1]+1 not in a:
            a[L-1] += 1

    print(*a)


if __name__ == '__main__':
    main()
