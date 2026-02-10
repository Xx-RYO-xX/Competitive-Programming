import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, m, k = map(int, input().split())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))

    ans = 0

    sys.setrecursionlimit(10**9)

    def dfs(pos, cost, rieki):
        nonlocal ans
        ans = max(ans, rieki)
        for i in range(
            pos + 1,
            min(n, pos + k + 1),
        ):
            a, b = ab[i]
            if cost + b <= m:
                dfs(i, cost + b, rieki + a)

    for j in range(n):
        a, b = ab[j]
        dfs(j, b, a)

    print(ans)


if __name__ == "__main__":
    main()
