def main():
    import sys

    input = sys.stdin.readline
    n, m, s, k = map(int, input().split())
    g = [[] for _ in range(m+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    dist = [-1]*(n+1)
    import  

if __name__ == "__main__":
    main()
