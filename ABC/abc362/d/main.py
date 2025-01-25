def main():
    import networkx as nx
    import matplotlib.pyplot as plt
    
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    nodes = {i+1: a[i] for i in range(n)}
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    nx.set_node_attributes(graph, nodes, 'weight')
    edges = []
    for _ in range(m):
        u, v, b = map(int, input().split())
        edges.append((u, v, b))
    graph.add_weighted_edges_from(edges)

if __name__ == '__main__':
    main()