def main():
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())
    d = max(map(int, input().split()))
    ans = 0
    for _ in range(m):
        s, h = input().split()
        h = int(h)
        ans += h > d

    print(ans)


if __name__ == "__main__":
    main()
