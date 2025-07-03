import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    g = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    
    for i in range(1, n+1):
        print(f"{i}: {{{', '.join(map(str, g[i]))}}}")


if __name__ == '__main__':
    main()
