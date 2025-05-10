import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    # import matplotlib.pyplot as plt
    
    # def show(graph):
    #     # インタラクティブモードを有効にする
    #     plt.ion()
        
    #     # 描画領域とグラフの初期設定
    #     fig, ax = plt.subplots()
    #     pos = nx.spring_layout(graph)  # レイアウトを指定
        
    #     # グラフの描画
    #     nx.draw_networkx(graph, pos, ax=ax, with_labels=True, node_size=700, node_color='lightblue', font_size=12)
        
    #     # エッジの重みを描画
    #     labels = nx.get_edge_attributes(graph, 'weight')
    #     nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, ax=ax)
        
    #     # ドラッグ対象のノードを保持する変数
    #     dragged_node = None
        
    #     # マウスボタンを押した時のイベントハンドラ
    #     def on_press(event):
    #         nonlocal dragged_node
    #         if event.inaxes != ax: return
            
    #         # クリックした位置に最も近いノードを探す
    #         for node, (x, y) in pos.items():
    #             if abs(event.xdata - x) < 0.1 and abs(event.ydata - y) < 0.1:
    #                 dragged_node = node
    #                 break
        
    #     # マウスを動かした時のイベントハンドラ
    #     def on_motion(event):
    #         nonlocal dragged_node
    #         if dragged_node is None or event.inaxes != ax: return
            
    #         # ノードの位置を更新
    #         pos[dragged_node] = (event.xdata, event.ydata)
            
    #         # グラフを再描画
    #         ax.clear()
    #         nx.draw_networkx(graph, pos, ax=ax, with_labels=True, node_size=700, node_color='lightblue', font_size=12)
    #         nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, ax=ax)
    #         fig.canvas.draw_idle()
        
    #     # マウスボタンを離した時のイベントハンドラ
    #     def on_release(event):
    #         nonlocal dragged_node
    #         dragged_node = None
        
    #     # イベントハンドラを登録
    #     fig.canvas.mpl_connect('button_press_event', on_press)
    #     fig.canvas.mpl_connect('motion_notify_event', on_motion)
    #     fig.canvas.mpl_connect('button_release_event', on_release)
        
    #     plt.show(block=True)  # グラフウィンドウが閉じないようにブロックモードで表示


    
    n, q = map(int, input().split())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    graph.add_edges_from(edges)

    color = [0]*(n+1)
    lens = nx.single_source_shortest_path_length(graph, 1)
    for i in range(2, n+1):
        if lens[i]%2!= 0:
            color[i] = 1
    
    for _ in range(q):
        c, d = map(int, input().split())
        if color[c] == color[d]:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    sys.exit(main())
