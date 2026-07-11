def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    ans = 0
    j = 1
    for i in range(1, n + 1):
        j = max(i, j)
        while j + 1 <= n:
            print("? " + str(i) + " " + str(j + 1), flush=True)
            if "Yes" == input().rstrip():
                j += 1
            else:
                break
        ans += j - i

    print("! " + str(ans), flush=True)


if __name__ == "__main__":
    main()
