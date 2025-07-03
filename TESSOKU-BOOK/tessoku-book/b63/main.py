import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict, deque
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    g = defaultdict(set)
    line = input()
    for j in range(1, r):
        nline = input()
        for i in range(c):
            if line[i] == nline[i] == ".":
                g[(j, i)].add((j-1, i))
                g[(j-1, i)].add((j, i))
            if i != c-1 and nline[i] == nline[i+1] == ".":
                g[(j, i)].add((j, i+1))
                g[(j, i+1)].add((j, i))
        line = nline

    dist = defaultdict(lambda :-1)
    dist[(sy-1, sx-1)] = 0
    q = deque([(sy-1, sx-1)])
    while q:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos]+1
                q.append(nex)
            if nex == (gy-1, gx-1):
                print(dist[nex])
                return


if __name__ == '__main__':
    main()
