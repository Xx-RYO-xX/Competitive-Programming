import sys


def input():return sys.stdin.readline().rstrip()


def main():
    while True:
        n = int(input())
        if n == 0: return
        a = list(map(int, input().split()))
        min_sa = (float("inf"), 0)
        for i in range(n):
            sa = abs(a[i]-2023)
            if min_sa[0] > sa:
                min_sa = (sa, i+1)
        print(min_sa[1])


if __name__ == '__main__':
    main()
