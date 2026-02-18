import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, l, w = map(int, input().split())
    d = list(map(int, input().split()))
    ans = 0
    for D in d:
        if l - w <= D <= l + w:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
