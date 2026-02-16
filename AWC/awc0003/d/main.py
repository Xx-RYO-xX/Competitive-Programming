import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate

    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    accm = [0] + list(accumulate(a))
    for i in range(1, n - k + 2):
        left = i + k - 1
        right = n
        find = -1

        while left <= right:
            mid = (left + right) // 2
            if accm[mid] - accm[i - 1] >= m:
                find = mid
                right = mid - 1
            else:
                left = mid + 1

        if find != -1:
            ans += n - find + 1

    print(ans)


if __name__ == "__main__":
    main()
