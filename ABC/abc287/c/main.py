import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import networkx as nx

    n, m = map(int, input().split())
    g = nx.Graph()
    g.add_nodes_from(range(1, n + 1))
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    degrees = [d for _, d in g.degree()]
    print(
        "Yes"
        if nx.is_connected(g) and degrees.count(1) == 2 and degrees.count(2) == n - 2
        else "No"
    )


if __name__ == "__main__":
    main()
