import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    x, y, l, r, a, b = map(int, input().split())
    ans = 0
    for i in range(a + 1, b + 1):
        if l < i <= r:
            ans += x
        else:
            ans += y

    print(ans)


if __name__ == "__main__":
    main()
