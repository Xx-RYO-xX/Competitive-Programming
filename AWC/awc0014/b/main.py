import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, v = map(int, input().split())
    d = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n - 2):
        d[i + 1] += d[i]

    ans = []
    for i in range(n - 1):
        if d[i] < t[i] * v:
            ans.append(i + 2)

    if ans:
        print(*ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
