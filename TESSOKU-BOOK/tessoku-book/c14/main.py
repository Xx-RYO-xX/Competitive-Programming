import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    import matplotlib.pyplot as plt
    
    
    n, m = map(int, input().split())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edge = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge.append((a, b, c))
    graph.add_weighted_edges_from(edge)

    ans = nx.dijkstra_path(G=graph, source=1, target=n, weight="weight")

    print(len(ans))

    def show(graph):
        pos = nx.spring_layout(graph)  # レイアウトを指定

        # グラフの描画
        nx.draw_networkx(graph, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12)

        # エッジの重みを描画
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.show()  # グラフを表示
    show(graph)


if __name__ == '__main__':
    main()
