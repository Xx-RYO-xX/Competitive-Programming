def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    eat = 0
    eated = [False] * (n + 1)
    for i in range(1, n + 1):
        l = max(i - m + 1, 1) - 1
        eat -= a[l] if eated[l] else 0
        if eat + a[i] <= k:
            eat = eat + a[i]
            eated[i] = True
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
