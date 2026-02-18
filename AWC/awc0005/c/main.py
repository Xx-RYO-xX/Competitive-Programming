import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a_sort = []
    for i in range(n):
        a_sort.append((a[i], i))
    a_sort = SortedList(a_sort)

    ans = 0
    while a_sort:
        num, i = a_sort.pop()
        target_idx = []
        if 0 < i:
            target_idx.append(i - 1)
        if i < n - 1:
            target_idx.append(i + 1)
        for idx in target_idx:
            if abs(a[i] - a[idx]) > k:
                a_sort.discard((a[idx], idx))
                ans += a[i] - k - a[idx]
                a[idx] = a[i] - k
                a_sort.add((a[idx], idx))

    print(ans)


if __name__ == "__main__":
    main()
