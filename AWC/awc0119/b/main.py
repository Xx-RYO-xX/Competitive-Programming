def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n - 1):
        ans += (i + 1) * b[i]

    print(ans)


if __name__ == "__main__":
    main()
