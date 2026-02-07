import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    for _ in range(int(input())):
        n = int(input())
        r = list(map(int, input().split()))
        r_sort = []
        for i in range(n):
            r_sort.append((r[i], i))
        r_sort = SortedList(r_sort)
        ans = 0
        while r_sort:
            gyo, i = r_sort.pop(0)
            target_idx = []
            if 0 < i:
                target_idx.append(i - 1)
            if i < n - 1:
                target_idx.append(i + 1)
            for idx in target_idx:
                if abs(r[idx] - r[i]) > 1:
                    r_sort.discard((r[idx], idx))
                    ans += r[idx] - (r[i] + 1)
                    r[idx] = r[i] + 1
                    r_sort.add((r[idx], idx))

        print(ans)


if __name__ == "__main__":
    main()
