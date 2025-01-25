import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    a, b, x, y = map(int, input().split())
    
    tatemono = nx.Graph()
    tatemono.add_nodes_from("a"+str(i) for i in range(1, 101))
    tatemono.add_nodes_from("b"+str(i) for i in range(1, 101))
    edges = []
    for i in range(1, 101):
        edges.append(("a"+str(i), "b"+str(i), x))
        if i != 100:
            edges.append(("a"+str(i+1), "b"+str(i), x))
            
            edges.append(("a"+str(i+1), "a"+str(i), y))
            edges.append(("b"+str(i+1), "b"+str(i), y))
    
    tatemono.add_weighted_edges_from(edges)
    
    print(nx.dijkstra_path_length(G=tatemono, source="a"+str(a), target="b"+str(b)))


if __name__ == '__main__':
    main()
