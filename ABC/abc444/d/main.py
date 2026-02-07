import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = sorted(map(int, input().split()))

    ans = []
    prev = 0
    for i in range(n):
        if prev == a[i]:
            continue
        for _ in range(a[i] - prev):
            ans.append(n - i)
        prev = a[i]

    i = 0
    while i < len(ans):
        if ans[i] >= 10:
            if i == len(ans) - 1:
                ans.append(0)
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
        i += 1

    print(*ans[::-1], sep="")


if __name__ == "__main__":
    main()
