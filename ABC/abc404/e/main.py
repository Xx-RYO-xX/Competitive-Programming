import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx

    

    
    n = int(input())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    g = nx.DiGraph()
    g.add_nodes_from(range(n))
    edges = []
    for i in range(1, n):
        for cc in range(-c[i-1], 0):
            edges.append((i, i+cc))
    g.add_edges_from(edges)

    
    ans = 0
    for i in range(1, n):
        if a[i-1] != 0:
            dist = nx.shortest_path_length(g, source=i, target=0)
            ans += dist

    print(ans)

if __name__ == '__main__':
    sys.exit(main())
