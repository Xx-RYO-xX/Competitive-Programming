import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    n, m = map(int, input().split())
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))
    egdes = []
    for _ in range(m):
        a, b = map(int, input().split())
        egdes.append((a, b))
    g.add_edges_from(egdes)


    if m != n:
        print("No")
        return

    for v in g.nodes():
        if g.degree(v) != 2:
            print("No")
            return
    if nx.is_connected(g):
        print("Yes")
    else:
        print("No")
    

if __name__ == '__main__':
    sys.exit(main())
