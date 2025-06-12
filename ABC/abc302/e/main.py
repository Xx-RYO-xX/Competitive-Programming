def main():
    from collections import defaultdict
    n, q = map(int, input().split())
    graph_set = defaultdict(set)
    for _ in range(q):
        query = input()
        if query[0] == "1":
            tmp, u, v = map(int, query.split())
            graph_set[u].add(v)
            graph_set[v].add(u)
        else:
            tmp, v = map(int,query.split())
            for G in graph_set[v]:
                # print(G)
                graph_set[G].discard(v)
                if len(graph_set[G]) == 0:
                    graph_set.pop(G)
            graph_set.pop(v, "")
        
        print(n - len(graph_set))

if __name__ == '__main__':
    main()
