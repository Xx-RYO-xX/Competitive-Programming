import sys
import networkx as nx

def input(): return sys.stdin.readline().rstrip()

def dfs(node, parent, graph, weights, dp_min, dp_max):
    total_min = 0
    total_max = 0
    for neighbor in graph.neighbors(node):
        if neighbor != parent:
            dfs(neighbor, node, graph, weights, dp_min, dp_max)
            total_min += dp_min[neighbor]
            total_max += dp_max[neighbor]
    dp_min[node] = weights[node] + total_min
    dp_max[node] = weights[node] + total_max

def main():
    n = int(input())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    graph.add_edges_from(edges)
    weights = [0] + list(map(int, input().split()))
    
    dp_min = [0] * (n + 1)
    dp_max = [0] * (n + 1)
    
    dfs(1, -1, graph, weights, dp_min, dp_max)
    
    print(dp_min[1], dp_max[1])

if __name__ == '__main__':
    sys.exit(main())
