import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    from collections import defaultdict

    n, t = map(int, input().split())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    graph.add_edges_from(edges)
    
    # nx.draw_networkx(graph)
    # plt.show()
    

    digraph = nx.DiGraph()
    digraph.add_nodes_from(graph.nodes())

    bfs_tree = nx.bfs_tree(graph, t)
    digraph.add_edges_from(bfs_tree.edges())
    
    # nx.draw_networkx(digraph)
    # plt.show()
    
    ans = defaultdict(int)
    def calc_rank(node):
        sons = list(digraph.successors(node))
        if not sons:
            ans[node] = 0
        else:
            max_rank = max(calc_rank(son) for son in sons)
            ans[node] = max_rank + 1
        return ans[node]
    
    calc_rank(1)
    for i in range(1, n+1):
        print(ans[i], end=" ")


if __name__ == '__main__':
    main()
