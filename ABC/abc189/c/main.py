import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for l in range(n):
        mins = a[l]
        for r in range(l, n):
            if mins > a[r]:
                mins = a[r]
            ans = max(ans, mins * (r - l + 1))
    print(ans)


if __name__ == "__main__":
    main()
