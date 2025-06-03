import sys 
import networkx as nx
# import matplotlib.pyplot as plt

def input():return sys.stdin.readline().rstrip()



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


def main():

    h, w = map(int, input().split())
    cost = nx.DiGraph()
    cost.add_nodes_from(range(10))
    edges = []
    for i in range(10):
        c = list(map(int, input().split()))
        for j in range(10):
            edges.append((i, j, c[j]))
    cost.add_weighted_edges_from(edges)
    
    # show(cost)
    dist = dict(nx.floyd_warshall(cost, weight='weight'))
    ans = 0
    for hh in range(h):
        hhh = list(map(int, input().split()))
        for ww in range(w):
            if hhh[ww] != -1 and hhh[ww] != 1:
                ans += dist[hhh[ww]][1]
    

    print(ans)

if __name__ == '__main__':
    sys.exit(main())
