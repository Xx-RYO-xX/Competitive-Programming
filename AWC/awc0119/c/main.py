def main():
    import sys

    input = sys.stdin.readline

    n, m, a = map(int, input().split())
    h = list(map(int, input().split()))

    ans = 0
    for H in h:
        if H <= a:
            continue
        elif H <= m:
            ans += 1
            m //= 2
        else:
            print(-1)
            return

    print(ans)


if __name__ == "__main__":
    main()
