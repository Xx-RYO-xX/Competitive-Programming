import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    import matplotlib.pyplot as plt
    

    n = int(input())
    tree = nx.Graph()
    tree.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    tree.add_edges_from(edges)
    
    # nx.draw_networkx(tree)
    # plt.show()
    

if __name__ == '__main__':
    sys.exit(main())
