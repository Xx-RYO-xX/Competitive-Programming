import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    from sortedcontainers import SortedList
    from bisect import bisect_right
    
    n, m = map(int, input().split())
    graph = defaultdict(SortedList)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    
    ans = 0
    for i in range(1, n+1):
        lst = graph[i]
        if bisect_right(lst, i) == 1:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
