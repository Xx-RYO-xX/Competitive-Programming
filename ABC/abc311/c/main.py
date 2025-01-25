def main():
    import networkx as nx
    # import matplotlib.pyplot as plt

    n = int(input())
    a = list(map(int, input().split()))
    
    graph = nx.DiGraph()
    edge = [(i+1, a[i]) for i in range(n)]
    # print(edge)
    graph.add_edges_from(edge)
    
    a = list(nx.strongly_connected_components(graph))
    
    for A in a:
        if len(A) != 0:
            aa = list(A)
            # print(aa)
            ans1 = nx.shortest_path(graph, source=aa[0], target=aa[-1]) 
            ans2 = nx.shortest_path(graph, source=aa[0], target=aa[1])
            if len(ans1) < len(ans2):
                print(len(ans2))
                print(*ans2)
            else:
                print(len(ans1))
                print(*ans1)
            exit()
    
    # nx.draw_networkx(graph)
    # plt.show()
    
    

if __name__ == '__main__':
    main()
