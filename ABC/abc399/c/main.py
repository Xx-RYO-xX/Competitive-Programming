import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    n, m = map(int, input().split())
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    g.add_edges_from(edges)
    
    if nx.is_forest(g):
        print(0)
        return

    cut = nx.number_connected_components(g)
    ans = m-(n-cut)
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
