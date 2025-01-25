import sys


def main():
    import networkx as nx

    t = int(input())
    for T in range(1, t+1):
        print("Case #%d:" % T)
        n, m = map(int, input().split())
        graph = nx.DiGraph()
        graph.add_nodes_from(range(1, n+1))
        edges = []
        for _ in range(m):
            a, b = map(int, input().split())
            edges.append((a, b))
        graph.add_edges_from(edges)

        kyosan_cycle = nx.strongly_connected_components(graph)

        ans = 0
        for KC in kyosan_cycle:
            if 2 <= len(KC):
                ans += len(KC)
        
        print(ans if ans != 0 else "Happy")


if __name__ == '__main__':
    main()
