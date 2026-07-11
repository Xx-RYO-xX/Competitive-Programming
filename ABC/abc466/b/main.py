def main():
    import sys

    input = sys.stdin.readline

    from collections import defaultdict

    n, m = map(int, input().split())
    ans = defaultdict(lambda: -1)

    for _ in range(n):
        c, s = map(int, input().split())
        ans[c] = max(ans[c], s)

    for i in range(1, m + 1):
        print(ans[i], end=" ")


if __name__ == "__main__":
    main()
