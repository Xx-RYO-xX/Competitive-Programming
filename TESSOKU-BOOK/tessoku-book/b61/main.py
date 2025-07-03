import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    n, m = map(int, input().split())
    g = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].add(b)
        g[b].add(a)
    
    ans = (0, 0)
    for i in g:
        ans = max((len(g[i]), i), ans)
    print(ans[1])

if __name__ == '__main__':
    main()
