import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict

    n, q = map(int, input().split())
    g = defaultdict(set)
    for _ in range(q):
        query = input()
        if query[0] == "1":
            que, u, v = map(int, query.split())
            g[u].add(v)
            g[v].add(u)

        else:
            que, v = map(int, query.split())
            try:
                for u in g.pop(v):
                    g[u].discard(v)
                    if len(g[u]) == 0:
                        g.pop(u)
            except:
                None

        print(n - len(g))


if __name__ == "__main__":
    main()
