import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n = int(input())

    cnt = defaultdict(int)
    x = 1
    while x * x * 2 < n:
        y = x + 1
        while True:
            good = x * x + y * y
            if good > n:
                break
            cnt[good] += 1
            y += 1

        x += 1

    ans = []
    for good in cnt:
        if cnt[good] == 1:
            ans.append(good)

    print(len(ans))
    print(*sorted(ans))


if __name__ == "__main__":
    main()
