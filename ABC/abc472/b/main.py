def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))

    ans = float("inf")
    for i in range(n):
        left = sum(l[0 : i + 1])
        right = sum(l[i + 1 :])
        ans = min(ans, abs(left - right))
    print(ans)


if __name__ == "__main__":
    main()
