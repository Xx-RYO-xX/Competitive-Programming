def main():
    import sys
    import heapq

    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        ab = []
        for i in range(n):
            a, b = map(int, input().split())
            ab.append((a, b))
        ab = sorted(ab, key=lambda x: x[0] - x[1], reverse=True)
        minidx = ab.index(min(ab))
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans += ab[i][1]
            else:
                ans += ab[i][0]

        for i in range(n // 2, n):
            anst = ans - ab[i][0] + ab[i][1] + ab[minidx][0]
            if ans > anst:
                ans = anst

        print(ans)


if __name__ == "__main__":
    main()
