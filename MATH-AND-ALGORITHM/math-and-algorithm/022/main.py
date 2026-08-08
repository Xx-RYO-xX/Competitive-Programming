import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = sorted(map(int, input().split()))

    from bisect import bisect_left, bisect_right

    # print(a)

    ans = 0
    for i in range(n):
        find = 100000 - a[i]
        left_idx = bisect_left(a, find, lo=i + 1)
        if left_idx == len(a) or a[left_idx] != find:
            continue

        right_idx = bisect_right(a, find) - 1
        ans += right_idx - left_idx + 1
        # print(left_idx, right_idx, i)
        # print(ans)

    print(ans)


if __name__ == "__main__":
    main()
