def main():
    import sys

    input = sys.stdin.readline

    m, d = map(int, input().split())
    s = list(input())[:-1]

    ans = [True] * m
    g = []
    for i in range(m):
        if s[i] == "G":
            g.append(i)

    for G in g:
        for i in range(m):
            if abs(i - G) <= d:
                ans[i] = False

    print(sum(ans))


if __name__ == "__main__":
    main()
