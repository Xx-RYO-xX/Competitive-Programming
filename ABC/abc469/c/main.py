def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    s = list(input())[:-1]

    xx = []
    for i in range(n):
        if s[i] == "x":
            xx.append(i + 1)

    ans = []
    for k in range(1, n + 1):
        if k <= len(xx):
            ans.append(str(xx[k - 1]))
        else:
            ans.append(str(n))

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
