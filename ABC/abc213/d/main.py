import sys 


def input():return sys.stdin.readline().rstrip()




def main():
    from collections import defaultdict
    from sortedcontainers import SortedList
    n = int(input())
    g_lst = defaultdict(SortedList)
    for _ in range(n-1):
        a, b = map(int, input().split())
        g_lst[a].add(b)
        g_lst[b].add(a)
    print(g_lst)
    
    def dfs(pos, graph_lst, visited, path, goal):
        global finished
        if finished:
            return

        path.append(pos)
        visited[pos] = True
        if pos == goal:
            finished = True
            return

        for i in graph_lst[pos]:
            if not visited[i]:
                dfs(i, graph_lst, visited, path, goal)
                if finished:
                    return

        path.pop()
    
    print()
    dfs(1, )




if __name__ == '__main__':
    sys.exit(main())
