import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    n, m = map(int, input().split())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    ans_tree = nx.maximum_flow(graph)
    
    print(graph)


if __name__ == '__main__':
    main()
