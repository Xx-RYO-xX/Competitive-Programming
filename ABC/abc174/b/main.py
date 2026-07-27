def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        ans += x**2 + y**2 <= d**2

    print(ans)


if __name__ == "__main__":
    main()
