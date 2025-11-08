import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import Counter

    n = int(input())
    a = Counter(map(int, input().split()))

    ans = 0
    for A in a:
        num = a[A]
        if 2 <= num:
            ans += (num * (num - 1) // 2) * (n - num)

    print(ans)


if __name__ == "__main__":
    main()
