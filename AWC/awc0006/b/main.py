import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k, t = map(int, input().split())
    ans = 0
    for _ in range(n):
        d, r = map(int, input().split())
        if r >= k * d:
            ans += r

    print("Yes" if ans >= t else "No")


if __name__ == "__main__":
    main()
