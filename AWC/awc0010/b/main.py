import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    n = int(input())
    d = list(map(int, input().split()))

    ans = d[0]
    for i in range(1, n):
        if d[i - 1] < d[i]:
            ans += d[i] // 2
        else:
            ans += d[i]

    print(ans)


if __name__ == "__main__":
    main()
