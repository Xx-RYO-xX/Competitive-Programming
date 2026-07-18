def main():
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    aa = a.copy()
    ans = 0
    for i in range(n - 1):
        if (a[i] + a[i + 1]) % 2 != b[i]:
            ans += 1
            a[i + 1] = (a[i + 1] + 1) % 2

    ans2 = 1
    aa[0] = (aa[0] + 1) % 2
    for i in range(n - 1):
        if (aa[i] + aa[i + 1]) % 2 != b[i]:
            ans2 += 1
            aa[i + 1] = (aa[i + 1] + 1) % 2

    print(min(ans, ans2))


if __name__ == "__main__":
    main()
