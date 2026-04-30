import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += (b * (b + 1) // 2) - ((a - 1) * a // 2)

    print(ans)


if __name__ == "__main__":
    main()
