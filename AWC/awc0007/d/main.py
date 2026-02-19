import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, a, b = map(int, input().split())
    takahashi = list([False for _ in range(n)] for __ in range(n))
    aoki = list([False for _ in range(n)] for __ in range(n))

    def oou(r1, c1, r2, c2, is_takahashi=True):
        for r in range(r1 - 1, r2):
            for c in range(c1 - 1, c2):
                if is_takahashi:
                    takahashi[r][c] = True
                else:
                    aoki[r][c] = True

    for _ in range(a):
        r1, c1, r2, c2 = map(int, input().split())
        oou(r1, c1, r2, c2)
    for _ in range(b):
        r1, c1, r2, c2 = map(int, input().split())
        oou(r1, c1, r2, c2, False)

    ans = 0
    for r in range(n):
        for c in range(n):
            if takahashi[r][c] and aoki[r][c]:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
