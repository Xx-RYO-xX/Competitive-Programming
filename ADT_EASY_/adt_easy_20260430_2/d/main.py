import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, m = map(int, input().split())
    g = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)

    ans = 0
    for a in range(n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if a in g[b] and b in g[c] and c in g[a]:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
