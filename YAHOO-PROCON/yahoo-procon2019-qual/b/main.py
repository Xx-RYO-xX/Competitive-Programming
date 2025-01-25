import sys 

def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    graph = nx.Graph()
    graph.add_nodes_from(range(1, 5))
    edge = []
    for i in range(3):
        a, b = map(int, input().split())
        edge.append((a, b))
    graph.add_edges_from(edge)
    
    if nx.has_eulerian_path(graph):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    sys.exit(main())
