import networkx as nx
import matplotlib.pyplot as plt


def show(graph):
    pos = nx.spring_layout(graph)  # レイアウトを指定

    # グラフの描画
    nx.draw_networkx(graph, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12)

    # エッジの重みを描画
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()  # グラフを表示


def main():    
    n = int(input())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edge = []
    for i in range(1, n):
        d = list(map(int, input().split()))
        for j in range(i+1, n+1):
            edge.append((i, j, d[j-i-1]))
    graph.add_weighted_edges_from(edge)
    
    show(graph)


if __name__ == '__main__':
    main()