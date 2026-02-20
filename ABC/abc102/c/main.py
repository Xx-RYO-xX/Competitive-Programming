import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    Aii = []

    for i in range(n):
        Aii.append(a[i] - i)

    Aii.sort()

    ans = 0
    for i in range(n):
        ans += abs(Aii[n // 2] - (a[i] - i))

    print(ans)


if __name__ == "__main__":
    main()
