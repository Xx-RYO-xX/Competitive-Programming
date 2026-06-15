import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import networkx as nx

    n, m, t = map(int, input().split())
    g = nx.Graph()
    g.add_nodes_from(range(1, n + 1))
    abc = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        abc.append((a, b, c))
    g.add_weighted_edges_from(abc)

    try:
        ans = nx.dijkstra_path_length(G=g, source=1, target=t)

        print(2 * ans)
    except:
        print(-1)


if __name__ == "__main__":
    main()
