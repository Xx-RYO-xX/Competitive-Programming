import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from math import ceil

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    left = 0
    right = 10**19
    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for i in range(n):
            if a[i] < mid:
                cnt += (mid - a[i] + i + 1 - 1) // (i + 1)

        if cnt <= k:
            left = mid + 1
        else:
            right = mid - 1

    print(right)


if __name__ == "__main__":
    main()
