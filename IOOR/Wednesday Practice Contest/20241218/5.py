def main():
    import networkx as nx
    n, m = map(int, input().split())
    graph = nx.Graph()
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    graph.add_edges_from(edges)
    
    try:
        path_len = nx.dijkstra_path_length(G=graph, source=1, target=n)
        if path_len <= 2:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")
    except nx.NetworkXNoPath:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()