import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, t = map(int, input().split())
    h = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += c[i] if h[i] <= t else 0

    print(ans)


if __name__ == "__main__":
    main()
