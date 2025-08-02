import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))

    anset = defaultdict(int)
    ans = 0
    for j in range(n):
        val_j = (j+1)-a[j]
        ans += anset[val_j]

        val_i = (j+1)+a[j]
        anset[val_i] += 1

    print(ans)


if __name__ == '__main__':
    main()
