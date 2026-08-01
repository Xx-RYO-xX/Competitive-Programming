def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    s = list(input())[:-1]

    ans = 0
    for i in range(n):
        if s[i] == "x":
            if i - 1 == -1 or s[i - 1] == "x":
                if i + 1 == n or s[i + 1] == "x":
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
