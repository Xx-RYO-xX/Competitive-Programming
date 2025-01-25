import sys 

sys.setrecursionlimit(10**9)

def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    # import matplotlib.pyplot as plt
    from collections import defaultdict
    
    n = int(input())
    a = list(map(int, input().split()))
    graph = nx.DiGraph()
    graph.add_nodes_from(range(1, n+1))
    edges = []
    for i in range(2, n+1):
        edges.append((a[i-2], i))
    graph.add_edges_from(edges)
    
    ans = defaultdict(int)
    def count_sun(node):
        for son in graph.successors(node):
            if ans[son] == 0:
                ans[son] = count_sun(son)
            ans[node] += ans[son] + 1
        return ans[node]
    
    count_sun(1)
    for i in range(1, n+1):
        print(ans[i], end=' ')
    # nx.draw_networkx(graph)
    # plt.show()
    


if __name__ == '__main__':
    main()
