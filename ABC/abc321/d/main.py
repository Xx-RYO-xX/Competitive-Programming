import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from itertools import accumulate

    n, m, p = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    b_accm = list(accumulate(b))

    ans = 0
    for A in a:
        left = 0
        right = m

        while left < right:
            mid = (left + right) // 2
            if A + b[mid] < p:
                left = mid + 1
            else:
                right = mid
        # print(left)
        ans += p * (m - left)
        # print(ans)
        ans += A * left + b_accm[left - 1] if left != 0 else 0
        # print(ans)
    print(ans)


if __name__ == "__main__":
    sys.exit(main())
