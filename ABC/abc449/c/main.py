import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import bisect

    n, l, r = map(int, input().split())
    s = input()

    cnt = defaultdict(list)
    for i in range(n):
        cnt[s[i]].append(i)

    ans = 0
    for i in range(n):
        ss = s[i]
        left_idx = bisect.bisect_left(cnt[ss], i + l)
        right_idx = bisect.bisect_right(cnt[ss], i + r)
        ans += right_idx - left_idx

    print(ans)


if __name__ == "__main__":
    main()
