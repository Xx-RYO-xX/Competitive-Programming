def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    x = list(map(int, input().split()))

    ans = []
    for i in range(n):
        cond = True
        for j in range(n):
            if i != j and abs(x[i] - x[j]) < d:
                cond = False
        if cond:
            ans.append(i + 1)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
