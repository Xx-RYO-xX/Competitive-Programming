def main():
    import sys

    input = sys.stdin.readline

    s = list(input())[:-1]
    n = len(s)

    ans = 0
    for i in range(n):
        l = i
        r = i
        kakikae = 0
        while 0 <= l and r < n:
            if s[l] == s[r]:
                pass
            elif kakikae == 0:
                kakikae += 1
                pass
            else:
                break

            ans += 1
            l -= 1
            r += 1

    for i in range(n - 1):
        l = i
        r = i + 1
        kakikae = 0
        while 0 <= l and r < n:
            if s[l] == s[r]:
                pass
            elif kakikae == 0:
                kakikae += 1
                pass
            else:
                break

            ans += 1
            l -= 1
            r += 1

    print(ans)


if __name__ == "__main__":
    main()
