import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    zekkenn_hito = defaultdict(int)
    for i in range(n):
        zekkenn_hito[q[i]] = p[i]

    for i in range(1, n+1):
        print(q[zekkenn_hito[i]-1], sep=" ")


if __name__ == '__main__':
    sys.exit(main())
