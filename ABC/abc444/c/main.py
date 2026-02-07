import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedList

    n = int(input())
    a = SortedList(map(int, input().split()))

    ans = []

    def bis(l):
        aa = a.copy()
        while aa:
            val = aa.pop(0)
            if val == l:
                continue

            pair = l - val
            idx = aa.bisect_left(pair)
            if idx < len(aa) and aa[idx] == pair:
                aa.pop(idx)
            else:
                return
        ans.append(l)

    bis(a[-1])
    bis(a[-1] + a[0])

    print(*sorted(ans))


if __name__ == "__main__":
    main()
