import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cnt_a = Counter(a)

    ans = []
    for key, val in cnt_a.items():
        ans.append(key * val)

    if len(ans) <= k:
        print(0)
        return

    ans.sort()
    for i in range(k):
        ans.pop()

    print(sum(ans))


if __name__ == "__main__":
    main()
