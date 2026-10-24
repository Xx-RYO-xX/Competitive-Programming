def main():
    import sys

    input = sys.stdin.readline
    n, x = map(int, input().split())
    s = list(map(int, input().split()))

    ans = 0
    for S in s:
        if S <= x:
            ans += S
    print(ans)

if __name__ == "__main__":
    main()
