import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import matplotlib.pyplot as plt
    import networkx as nx
    
    n, m = map(int, input().split())
    graph = nx.Graph()
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    graph.add_weighted_edges_from(edges)
    



if __name__ == '__main__':
    main()
