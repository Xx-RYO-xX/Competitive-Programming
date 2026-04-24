import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter(a)
    ans = 0
    for num in cnt.values():
        if num >= 2:
            ans += (num * (num - 1) // 2) * (n - num)

    print(ans)


if __name__ == "__main__":
    main()
