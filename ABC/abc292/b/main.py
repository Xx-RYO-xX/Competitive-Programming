import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, q = map(int, input().split())
    cnt = defaultdict(int)
    for _ in range(q):
        num, x = map(int, input().split())
        if num != 3:
            cnt[x] += num
        else:
            print("Yes" if cnt[x] >= 2 else "No")


if __name__ == "__main__":
    main()
