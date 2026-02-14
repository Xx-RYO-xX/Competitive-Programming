import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = set(map(int, input().split()))

    ans = [0, 0]
    for i in range(n):
        if i + 1 in b and a[i] < k:
            ans[0] += 1
            ans[1] += a[i]

    print(*ans)


if __name__ == "__main__":
    main()
