import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, t = map(int, input().split())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += max(a - b * t, 0)

    print(ans)


if __name__ == "__main__":
    main()
