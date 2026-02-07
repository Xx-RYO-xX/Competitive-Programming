import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())

    ans = 0
    mame = n
    while mame < k:
        n += 1
        ans += 1
        mame += n

    print(ans)


if __name__ == "__main__":
    main()
