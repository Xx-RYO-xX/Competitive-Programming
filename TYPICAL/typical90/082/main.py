import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    MOD = 10**9 + 7
    l, r = map(int, input().split())

    def solve(n):
        if n <= 0:
            return 0
        ans = 0
        start = 1
        d = 1
        while start <= n:
            end = min(n, 10**d - 1)
            cnt = end - start + 1
            s = (start + end) * cnt // 2
            ans = (ans + d * s) % MOD
            start = end + 1
            d += 1
        return ans

    print((solve(r) - solve(l - 1)) % MOD)


if __name__ == '__main__':
    sys.exit(main())
