import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    import matplotlib.pyplot as plt
    
    n, m = map(int, input().split())
    a = list(map(int, input().split())) if m != 0 else []
    
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))
    edges = []
    for i in range(m):
        edges.append((a[i], a[i]+1))
    g.add_edges_from(edges)
    
    nx.draw_networkx(g)
    plt.show()
    


if __name__ == '__main__':
    main()
