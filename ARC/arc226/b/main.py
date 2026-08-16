def main():
    import sys

    input = sys.stdin.readline

    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        sums = 0
        for i in range(m):
            sums += a[i] * 2**i
        # print(ave)
        ok = sums
        ng = 0

        def is_ok(youryou):
            hukuro = 0

        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid


if __name__ == "__main__":
    main()
