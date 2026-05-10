import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    for i in range(n - 1):
        ans.append(a[i + 1] - a[i])
    ans.append(k - a[-1] + a[0])
    ans.sort()
    print(sum(ans[: n - 1]))


if __name__ == "__main__":
    main()
