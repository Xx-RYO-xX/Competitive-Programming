import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import networkx as nx

    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        g = nx.Graph()
        g.add_nodes_from(range(1, n + 1))
        edges = []
        weight = dict()
        for i in range(n):
            u = i + 1
            v = a[i]
            w = b[i]
            if w >= 0:
                edges.append((u, v, w))
                u, v = sorted([u, v])
                weight[(u, v)] = w
        g.add_weighted_edges_from(edges)

        ans = 0
        for hen in nx.max_weight_matching(g):
            u, v = sorted(hen)
            ans += weight[(u, v)]
        print(ans)


if __name__ == "__main__":
    main()
