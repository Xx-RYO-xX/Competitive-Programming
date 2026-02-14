import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n
    for i in range(n)[::-1]:
        x = a[i] - 1
        if x == i:
            ans[i] = i + 1
        else:
            ans[i] = ans[x]

    print(*ans)


if __name__ == "__main__":
    main()
