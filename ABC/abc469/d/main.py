def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    ab = []
    for i in range(m):
        a, b = map(int, input().split())

        ab.append(set([a, b]))

    ans = set()
    for x in ab[0]:
        y = ab[0]
        for i in range(1, m):
            yy = y & ab[i]
            if len(yy) == 0:
                if x not in ab[i]:
                    break
                continue
            y = yy
        else:
            for yy in y:
                ans.add(tuple(sorted((x, yy))))

    print(len(ans))


if __name__ == "__main__":
    main()
