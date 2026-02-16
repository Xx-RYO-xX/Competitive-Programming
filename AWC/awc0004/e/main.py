import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    accm = [0]
    cnt = defaultdict(int)
    cnt[0] = 1
    ans = 0
    for i in range(n):
        item = accm[-1] + a[i]
        accm.append(item)
        ans += cnt[item - k]
        cnt[item] += 1

    print(ans)


if __name__ == "__main__":
    main()
