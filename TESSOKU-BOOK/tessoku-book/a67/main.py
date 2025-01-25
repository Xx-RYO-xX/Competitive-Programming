import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    # import matplotlib.pyplot as plt
    
    n, m = map(int, input().split())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edges = list()
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    graph.add_weighted_edges_from(edges)
    
    mst = nx.minimum_spanning_tree(graph)
    
    weights = nx.get_edge_attributes(mst, 'weight').values()
    ans = sum(weights)
    print(ans)

if __name__ == '__main__':
    main()
